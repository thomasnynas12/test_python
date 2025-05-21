from aiokafka import AIOKafkaProducer
from fastapi import Depends

async def get_kafka_producer() -> AIOKafkaProducer:
    producer = AIOKafkaProducer(bootstrap_servers="localhost:9092")
    await producer.start()
    try:
        yield producer
    finally:
        await producer.stop()