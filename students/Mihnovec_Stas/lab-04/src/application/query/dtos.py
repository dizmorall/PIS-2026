from dataclasses import dataclass

@dataclass(frozen=True)
class ComplaintDto:
    """Упрощенная модель для чтения (Query)"""
    id: str
    url: str
    status: str
    ai_score: int
    reviews_count: int