import pytest
from httpx import AsyncClient
from fastapi import FastAPI
from unittest.mock import AsyncMock

from presentation.api.main import app
from domain.models.application import ApplicationIn
from application.services.application_service import ApplicationService


@pytest.fixture
def test_app() -> FastAPI:
    return app


@pytest.fixture
async def client(test_app):
    async with AsyncClient(app=test_app, base_url="http://test") as ac:
        yield ac


@pytest.fixture
def mock_application_service(monkeypatch):
    mock_service = AsyncMock(spec=ApplicationService)

    monkeypatch.setattr("presentation.api.v1.routes.application.get_application_service", lambda: mock_service)
    return mock_service


@pytest.mark.asyncio
async def test_create_application(client, mock_application_service):
    payload = {
        "applicant_id": "user123",
        "amount": 1500,
        "term_months": 12
    }

    response = await client.post("/api/v1/application", json=payload)

    assert response.status_code == 202
    mock_application_service.publish_application.assert_awaited_once()


@pytest.mark.asyncio
async def test_get_application_status(client, mock_application_service):
    applicant_id = "user123"
    mock_application_service.get_application_status.return_value = {
        "applicant_id": applicant_id,
        "status": "approved"
    }

    response = await client.get(f"/api/v1/application/{applicant_id}")

    assert response.status_code == 200
    assert response.json()["status"] == "approved"
    mock_application_service.get_application_status.assert_awaited_once_with(applicant_id)
