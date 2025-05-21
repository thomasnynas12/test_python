from typing import AsyncGenerator
from aiokafka import AIOKafkaProducer
from app.infrastructure.db.repository import PostgresRepository
from app.infrastructure.redis.cache import RedisCache
from app.usecases.application_service import ApplicationService

KAFKA_BOOTSTRAP_SERVERS = "localhost:9092"

async def get_kafka_producer() -> AsyncGenerator[AIOKafkaProducer, None]:
    producer = AIOKafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)
    await producer.start()
    try:
        yield producer
    finally:
        await producer.stop()

def get_postgres_repository() -> PostgresRepository:
    return PostgresRepository()

def get_redis_cache() -> RedisCache:
    return RedisCache()

def get_application_service(
    repo: PostgresRepository = get_postgres_repository(),
) -> ApplicationService:
    return ApplicationService(repo)