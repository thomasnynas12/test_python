import asyncio, json
from aiokafka import AIOKafkaConsumer
from app.domain.entities import LoanApplication
from app.usecases.application_service import ApplicationService
from app.infrastructure.db.repository import PostgresRepository
from app.infrastructure.redis.cache import RedisCache

async def consume():
    consumer = AIOKafkaConsumer(
        "loan_applications", bootstrap_servers="localhost:9092", group_id="loan_group"
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