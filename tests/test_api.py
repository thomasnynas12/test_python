import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_submit_and_get_application(mocker):
    # Mock Kafka producer's send_and_wait
    mocker.patch("app.interfaces.api.routes.get_kafka_producer", return_value=DummyProducer())

    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Test POST /application
        response = await ac.post("/application", json={
            "applicant_id": "test123",
            "amount": 1000,
            "term_months": 12
        })
        assert response.status_code == 200
        assert response.json() == {"message": "Application submitted."}

        # Mock Redis cache and Postgres repository for GET /application/test123
        mocker.patch("app.interfaces.api.routes.RedisCache.get", return_value="approved")
        response = await ac.get("/application/test123")
        assert response.status_code == 200
        assert response.json() == {"status": "approved"}

class DummyProducer:
    async def send_and_wait(self, topic, message):
        return None
