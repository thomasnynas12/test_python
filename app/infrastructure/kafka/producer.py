from typing import AsyncGenerator
from aiokafka import AIOKafkaProducer
from app.domain.config import KAFKA_BOOTSTRAP_SERVERS

async def get_kafka_producer() -> AsyncGenerator[AIOKafkaProducer, None]:
    producer = AIOKafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)
    await producer.start()
    try:
        yield producer
    finally:
        await producer.stop()
