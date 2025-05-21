from app.domain.entities import LoanApplication
from app.domain.interfaces import ApplicationRepository
from app.domain.config import MIN_TERM_MONTHS, MAX_TERM_MONTHS, MAX_APPROVAL_AMOUNT

class ApplicationService:
    def __init__(self, repo: ApplicationRepository):
        self.repo = repo

def validate_application(self, app: LoanApplication) -> bool:
    return app.amount > 0 and MIN_TERM_MONTHS <= app.term_months <= MAX_TERM_MONTHS

def determine_status(self, app: LoanApplication) -> str:
    return "approved" if app.amount <= MAX_APPROVAL_AMOUNT else "rejected"