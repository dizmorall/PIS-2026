from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class DomainEvent:
    occurred_at: datetime = datetime.now()

@dataclass(frozen=True)
class ComplaintCreated(DomainEvent):
    complaint_id: str
    news_url: str

@dataclass(frozen=True)
class ComplaintClosedAsFake(DomainEvent):
    complaint_id: str
    reason: str

@dataclass(frozen=True)
class AIAnalysisAttached(DomainEvent):
    complaint_id: str
    score: int