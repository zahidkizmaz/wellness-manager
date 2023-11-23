from dataclasses import dataclass, field
from datetime import datetime

from .heartbeat import HeartBeat


@dataclass(kw_only=True, slots=True)
class HealthCheck:
    name: str
    title: str
    description: str = ""
    beats: list[HeartBeat] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)
