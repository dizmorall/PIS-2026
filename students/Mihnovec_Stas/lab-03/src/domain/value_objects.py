from dataclasses import dataclass
from typing import Optional
from urllib.parse import urlparse
from .exceptions import RuleViolationException

@dataclass(frozen=True)
class ComplaintId:
    """VO 1: Строго типизированный ID жалобы"""
    value: str
    
    def __post_init__(self):
        if not self.value or len(self.value) < 5:
            raise RuleViolationException("ID жалобы должен быть не короче 5 символов")

@dataclass(frozen=True)
class NewsUrl:
    """VO 2: URL новости"""
    url: str

    def __post_init__(self):
        result = urlparse(self.url)
        if not all([result.scheme, result.netloc]):
            raise RuleViolationException(f"Некорректный URL новости: {self.url}")
        if result.scheme not in ['http', 'https']:
            raise RuleViolationException("URL должен начинаться с http или https")

@dataclass(frozen=True)
class Reason:
    """VO 3: Причина жалобы"""
    category: str
    details: str

    def __post_init__(self):
        valid_categories = ["FAKE_NEWS", "HATE_SPEECH", "SCAM", "OTHER"]
        if self.category not in valid_categories:
            raise RuleViolationException(f"Неизвестная категория: {self.category}")
        if len(self.details) < 10:
            raise RuleViolationException("Детальное описание должно быть не менее 10 символов")

@dataclass(frozen=True)
class AIAnalysisResult:
    """VO 4: Результат проверки нейросетью"""
    fake_probability_score: int  # от 0 до 100
    flags: tuple  # Кортежи иммутабельны, в отличие от списков

    def __post_init__(self):
        if not (0 <= self.fake_probability_score <= 100):
            raise RuleViolationException("Score должен быть от 0 до 100")