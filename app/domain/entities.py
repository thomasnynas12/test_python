from dataclasses import dataclass

@dataclass
class LoanApplication:
    applicant_id: str
    amount: float
    term_months: int
