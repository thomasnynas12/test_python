
import pytest
from app.domain.entities import LoanApplication
from app.usecases.application_service import ApplicationService

@pytest.mark.asyncio
async def test_validate_application():
    service = ApplicationService(None)
    valid_app = LoanApplication("applicant1", 1000, 12)
    invalid_app = LoanApplication("applicant2", -100, 0)
    assert service.validate_application(valid_app) is True
    assert service.validate_application(invalid_app) is False

@pytest.mark.asyncio
async def test_determine_status():
    service = ApplicationService(None)
    low_amount = LoanApplication("applicant1", 1000, 12)
    high_amount = LoanApplication("applicant2", 6000, 12)
    assert service.determine_status(low_amount) == "approved"
    assert service.determine_status(high_amount) == "rejected"
