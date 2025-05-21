from app.domain.interfaces import ApplicationRepository
from app.domain.entities import LoanApplication
from .models import ApplicationModel
from .database import async_session
from sqlalchemy import select

class PostgresRepository(ApplicationRepository):
    async def save(self, app: LoanApplication, status: str):
        async with async_session() as session:
            session.add(ApplicationModel.from_entity(app, status))
            await session.commit()

    async def get_latest_status(self, applicant_id: str) -> str:
        async with async_session() as session:
            result = await session.execute(
                select(ApplicationModel.status).where(ApplicationModel.applicant_id == applicant_id)
            )
            row = result.first()
            return row[0] if row else None
