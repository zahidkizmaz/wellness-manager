from dataclasses import dataclass, field
from datetime import datetime


@dataclass(frozen=True, kw_only=True, slots=True)
class HeartBeat:
    name: str
    location: str
    finished_at: datetime | None = None
    created_at: datetime = field(default_factory=datetime.now)
