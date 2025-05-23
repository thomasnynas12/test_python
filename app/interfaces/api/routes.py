from fastapi import APIRouter, Depends, HTTPException
from app.domain.entities import LoanApplication
from app.infrastructure.kafka.producer import get_kafka_producer
from app.infrastructure.db.repository import PostgresRepository
from app.infrastructure.redis.cache import RedisCache
import json

router = APIRouter()

@router.post("/application")
async def submit_application(application: LoanApplication, producer=Depends(get_kafka_producer)):
    await producer.send_and_wait("loan_applications", json.dumps(application.__dict__).encode("utf-8"))
    return {"message": "Application submitted."}

@router.get("/application/{applicant_id}")
async def get_application_status(applicant_id: str):
    repo = PostgresRepository()
    cache = RedisCache()
    cached = await cache.get(applicant_id)
    if cached:
        return {"status": cached}
    db_status = await repo.get_latest_status(applicant_id)
    if not db_status:
        raise HTTPException(status_code=404, detail="Application not found")
    return {"status": db_status}
