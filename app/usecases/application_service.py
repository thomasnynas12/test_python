from app.domain.entities import LoanApplication
from app.domain.interfaces import ApplicationRepository

class ApplicationService:
    def __init__(self, repo: ApplicationRepository):
        self.repo = repo

    def validate_application(self, app: LoanApplication) -> bool:
        return app.amount > 0 and 1 <= app.term_months <= 60

    def determine_status(self, app: LoanApplication) -> str:
        return "approved" if app.amount <= 5000 else "rejected"
