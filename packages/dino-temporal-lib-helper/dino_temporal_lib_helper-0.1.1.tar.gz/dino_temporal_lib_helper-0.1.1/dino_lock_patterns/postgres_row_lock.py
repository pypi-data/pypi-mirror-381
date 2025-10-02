import math
import os
import random
import psycopg2
from contextlib import contextmanager
import threading
import time
from psycopg2.extras import Json
from psycopg2._psycopg import cursor

TABLE_NAME = os.getenv("DB_LOCK_TABLE", "locks")
# update_task_timeout
UPDATE_TASK_TIMEOUT = int(os.getenv("UPDATE_TASK_TIMEOUT", "1800"))  # 30 phút


class PostgresRowLocker:
    def __init__(self, dsn, table=TABLE_NAME):
        """
        dsn: PostgreSQL DSN connection string
             e.g. "dbname=test user=postgres password=secret host=localhost port=5432"
        table: table used to manage row locks
        """
        self.conn = psycopg2.connect(dsn)
        self.conn.autocommit = False
        self.table = table
        self._ensure_table()
        self._stop_event = threading.Event()

    def _ensure_table(self):
        """Create table + indexes if not exist"""
        with self.conn.cursor() as cur:
            cur.execute(f"""
                CREATE TABLE IF NOT EXISTS {self.table} (
                    id TEXT PRIMARY KEY,
                    status TEXT DEFAULT 'pending',
                    user_id TEXT DEFAULT NULL,
                    data JSONB DEFAULT '{{}}',
                    created_at TIMESTAMPTZ DEFAULT now()
                )
            """)

            # Index cho query kiểu WHERE status=... ORDER BY created_at
            cur.execute(f"""
                CREATE INDEX IF NOT EXISTS idx_{self.table}_status_created_at
                ON {self.table} (status, created_at DESC)
            """)

            # Index cho JSONB field "type"
            cur.execute(f"""
                CREATE INDEX IF NOT EXISTS idx_{self.table}_data_type
                ON {self.table} ((data->>'type'))
            """)
            # Index cho JSONB field "owner"
            cur.execute(f"""
                CREATE INDEX IF NOT EXISTS idx_{self.table}_data_owner
                ON {self.table} (user_id)
            """)
            # Index cho ORDER BY created_at DESC, id LIMIT 20
            cur.execute(f"""
                CREATE INDEX IF NOT EXISTS idx_{self.table}_created_at_id
                ON {self.table} (created_at DESC, id DESC)
            """)

            self.conn.commit()

    def update_workflow_status_timeout(self, timeout: int = UPDATE_TASK_TIMEOUT) -> list[dict] | None:
        """Update status to 'timeout' if created_at is older than timeout seconds"""
        try:
            with self.conn.cursor() as cur:
                cur.execute(
                    f"UPDATE {self.table} SET status='timeout' WHERE status='workflow_running' "
                    f"AND created_at < now() - interval '%s seconds'",
                    (timeout,)
                )
                self.conn.commit()
            return True
        except Exception as e:
            return None

    def loop_background_timeout(self, interval: int = 600, timeout: int = UPDATE_TASK_TIMEOUT):
        """Loop to update workflow status timeout in background"""

        def loop():
            time.sleep(random.randint(1, 10) * 10)
            while not self._stop_event.is_set():
                rows = self.update_workflow_status_timeout(timeout)
                # wait với khả năng stop sớm
                self._stop_event.wait(interval)

        t = threading.Thread(
            target=loop,
            daemon=True,
            name="PostgresRowLocker-TimeoutLoop"
        )
        t.start()
        return t

    def query(self, where_clause: str = "", select_clause: dict = None, params: tuple = (), limit: int = 20, offset: int = 0) -> list[dict]:
        """Query rows with optional where clause, select clause, limit and offset"""
        with self.conn.cursor() as cur:
            if not select_clause:
                select_clause = {
                    "id": "id",
                    "status": "status",
                    "user_id": "user_id",
                    "data": "data",
                    "created_at": "created_at"
                }

            selectors = []
            for key, value in select_clause.items():
                selectors.append(f"{value} AS {key}")
            select_sql = ", ".join(selectors)

            sql = f"SELECT {select_sql} FROM {self.table}"

            if where_clause:
                sql += f" WHERE {where_clause}"
            sql += " ORDER BY created_at DESC"
            if limit > 0:
                sql += f" LIMIT {limit}"
            if offset > 0:
                sql += f" OFFSET {offset}"
            cur.execute(sql, params)
            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            result = [dict(zip(columns, row)) for row in rows]
            return result

    def stop(self):
        """Stop background loop gracefully"""
        self._stop_event.set()

    @contextmanager
    def lock(self, id: str):
        """
        Acquire a row lock with SELECT FOR UPDATE.
        Returns SessionCursor + row.
        """
        with SessionCursor(self.conn, self.table, id) as session:
            try:
                session.cur.execute(
                    f"SELECT id,status,data,created_at FROM {self.table} WHERE id=%s FOR UPDATE", (id,)
                )
                row = session.cur.fetchone()
                print(f"[{threading.current_thread().name}] Locked row {id}")
                yield session, {
                    "id": row[0],
                    "status": row[1],
                    "data": row[2],
                    "created_at": row[3]
                } if row else None
                print(f"[{threading.current_thread().name}] Commit, lock released for {id}")
            except Exception:
                self.conn.rollback()
                print(f"[{threading.current_thread().name}] Rollback, lock released for {id}")
                raise

    def close(self):
        """Close the connection"""
        self.conn.close()


class SessionCursor:
    def __init__(self, conn, table, lock_id):
        self.conn = conn
        self.table = table
        self.lock_id = lock_id
        self.cur: cursor = None

    def __enter__(self):
        self.cur = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.conn.commit()
        else:
            self.conn.rollback()
        if self.cur:
            self.cur.close()
        self.cur = None

    # -----------------------------
    # CRUD operations
    # -----------------------------
    def upsert(self, data: dict | None = None):
        """Insert (or update) row data"""
        self.cur.execute(
            f"INSERT INTO {self.table} (id, data) VALUES (%s, %s) "
            f"ON CONFLICT (id) DO UPDATE SET data = EXCLUDED.data "
            f"RETURNING *",
            (self.lock_id, Json(data or {}))
        )
        return self.cur.fetchone()

    def delete(self):
        """Delete row"""
        self.cur.execute(f"DELETE FROM {self.table} WHERE id=%s RETURNING *", (self.lock_id,))
        return self.cur.fetchone()

    # -----------------------------
    # Status helpers
    # -----------------------------
    def update_status(self, status: str):
        self.cur.execute(
            f"UPDATE {self.table} SET status=%s WHERE id=%s RETURNING *",
            (status, self.lock_id)
        )
        return self.cur.fetchone()

    def status_cancel(self):
        return self.update_status("cancel")

    def status_done(self):
        return self.update_status("done")

    def status_workflow_running(self):
        return self.update_status("workflow_running")

    def is_status(self, status: str) -> bool:
        self.cur.execute(f"SELECT status FROM {self.table} WHERE id=%s", (self.lock_id,))
        row = self.cur.fetchone()
        return bool(row) and row[0] == status

    def is_cancelled(self) -> bool:
        return self.is_status("cancel")

    def is_pending(self) -> bool:
        return self.is_status("pending")

    def is_done(self) -> bool:
        return self.is_status("done")


# -----------------------------
# Example usage
# -----------------------------


def consumer(dsn, lock_id, sleep_time=5):
    locker = PostgresRowLocker(dsn)
    try:
        with locker.lock(lock_id) as (session, row):
            if not row:  # nếu row chưa có thì insert
                row = session.upsert({"owner": threading.current_thread().name})
                print(f"[{threading.current_thread().name}] Inserted {lock_id}: {row}")

            print(f"[{threading.current_thread().name}] Processing row {lock_id} ...")
            time.sleep(sleep_time)

            if not session.is_cancelled():
                session.status_done()
                print(f"[{threading.current_thread().name}] Marked {lock_id} as done")
            else:
                print(f"[{threading.current_thread().name}] {lock_id} was cancelled!")

            # Ví dụ: xoá row sau khi done
            if session.is_done():
                deleted = session.delete()
                print(f"[{threading.current_thread().name}] Deleted {lock_id}: {deleted}")
    finally:
        locker.close()


def get_postgres_locker(table=TABLE_NAME, dsn=None):
    if dsn is None:
        DB_HOST = os.getenv("DB_HOST", "localhost")
        DB_PORT = os.getenv("DB_PORT", "5432")
        DB_NAME = os.getenv("DB_NAME", "test")
        DB_USER = os.getenv("DB_USER", "postgres")
        DB_PASSWORD = os.getenv("DB_PASSWORD", "secret")
        dsn = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}"
    return PostgresRowLocker(dsn, table)


if __name__ == "__main__":
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "5432")
    DB_NAME = os.getenv("DB_NAME", "test")
    DB_USER = os.getenv("DB_USER", "postgres")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "secret")
    DSN = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}"

    t1 = threading.Thread(target=consumer, args=(DSN, "task-1", 5), name="Consumer-1")
    t2 = threading.Thread(target=consumer, args=(DSN, "task-1", 5), name="Consumer-2")
    t3 = threading.Thread(target=consumer, args=(DSN, "task-2", 3), name="Consumer-3")

    t1.start()
    time.sleep(1)  # cho t1 lock trước
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
