import asyncio, json
from aiokafka import AIOKafkaConsumer
from app.domain.entities import LoanApplication
from app.usecases.application_service import ApplicationService
from app.infrastructure.db.repository import PostgresRepository
from app.infrastructure.redis.cache import RedisCache
from app.config import settings

async def consume():
    consumer = AIOKafkaConsumer(
        settings.KAFKA_TOPIC,
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
        group_id=settings.KAFKA_GROUP_ID
    )
    await consumer.start()
    try:
        async for msg in consumer:
            data = json.loads(msg.value)
            application = LoanApplication(**data)
            repo = PostgresRepository()
            cache = RedisCache()
            service = ApplicationService(repo)

            if service.validate_application(application):
                status = service.determine_status(application)
                await repo.save(application, status)
                await cache.set(application.applicant_id, status)
    finally:
        await consumer.stop()