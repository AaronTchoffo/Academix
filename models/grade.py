from dataclasses import dataclass, field
from datetime import date
from typing import Optional

@dataclass
class Grade:
    id: Optional[int] = None
    student_id: int
    subject_id: int
    score: float
    evaluation_type: str = "Exam"
    evaluation_date: str = field(default_factory=lambda: date.today().isoformat())
    comment: Optional[str] = None