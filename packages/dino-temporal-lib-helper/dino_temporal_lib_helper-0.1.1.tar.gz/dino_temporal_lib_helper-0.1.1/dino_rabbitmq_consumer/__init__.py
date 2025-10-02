#!/usr/bin/env python3
"""
RabbitMQ Consumer Package for AI Audio Match
"""

from dino_rabbitmq_consumer.consumer import RabbitMQConsumer, start_rabbitmq_consumer, get_consumer_stats
from dino_rabbitmq_consumer.workflow_manager import WorkflowManager
from dino_rabbitmq_consumer.config import get_config, get_rabbitmq_url

__all__ = [
    "RabbitMQConsumer",
    "start_rabbitmq_consumer", 
    "get_consumer_stats",
    "WorkflowManager",
    "get_config",
    "get_rabbitmq_url"
]
