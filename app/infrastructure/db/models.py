from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Float, Integer

Base = declarative_base()

class ApplicationModel(Base):
    __tablename__ = "loan_applications"

    id = Column(String, primary_key=True, index=True)
    applicant_id = Column(String, index=True)
    amount = Column(Float)
    term_months = Column(Integer)
    status = Column(String)

    @staticmethod
    def from_entity(app, status):
        return ApplicationModel(
            id=app.applicant_id,
            applicant_id=app.applicant_id,
            amount=app.amount,
            term_months=app.term_months,
            status=status
        )