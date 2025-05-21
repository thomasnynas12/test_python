from fastapi import Depends
from app.infrastructure.db.repository import PostgresRepository
from app.infrastructure.redis.cache import RedisCache
from app.infrastructure.kafka.producer import get_kafka_producer

def get_repository():
    return PostgresRepository()

def get_cache():
    return RedisCache()

kafka_producer = get_kafka_producer
