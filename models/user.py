from dataclasses import dataclass, field
from datetime import date
from typing import Optional

@dataclass
class User:
    id: Optional[int] = None
    username: str = ""
    passworld_hash: Optional[str] = None
    creation_date: str = field(default_factory=lambda: date.today().isoformat())
    last_login: str = ""