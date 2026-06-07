from dataclasses import dataclass, field
from datetime import date
from typing import Optional

@dataclass
class Grade:
    student_id: str
    subject_id: int
    score: float
    
    id: Optional[int] = None
    evaluation_type: str = "Exam"
    evaluation_date: str = field(default_factory=lambda: date.today().isoformat())
    comment: Optional[str] = None