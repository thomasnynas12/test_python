from abc import ABC, abstractmethod
from .entities import LoanApplication

class ApplicationRepository(ABC):
    @abstractmethod
    async def save(self, application: LoanApplication, status: str): ...

    @abstractmethod
    async def get_latest_status(self, applicant_id: str) -> str: ...
