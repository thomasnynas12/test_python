from app.domain.entities import LoanApplication
from app.usecases.application_service import ApplicationService

def test_approval_logic():
    service = ApplicationService(None)
    app = LoanApplication("id123", 500, 12)
    assert service.determine_status(app) == "approved"
