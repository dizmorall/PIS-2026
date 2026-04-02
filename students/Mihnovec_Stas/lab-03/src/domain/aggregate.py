from typing import List, Optional
from datetime import datetime
from .value_objects import ComplaintId, NewsUrl, Reason, AIAnalysisResult
from .entities import Review
from .events import DomainEvent, ComplaintCreated, AIAnalysisAttached, ComplaintClosedAsFake
from .exceptions import InvalidComplaintStatusException, RuleViolationException

class Complaint:
    """Entity 3 & Aggregate Root: Жалоба"""
    
    # Константы для бизнес-логики
    AUTO_BLOCK_THRESHOLD = 95
    
    def __init__(self, c_id: ComplaintId, news_url: NewsUrl, reporter_id: str, reason: Reason):
        self._id = c_id
        self._news_url = news_url
        self._reporter_id = reporter_id
        self._reason = reason
        
        self._status = "PENDING"  # PENDING, IN_REVIEW, FAKE_CONFIRMED, REJECTED
        self._ai_result: Optional[AIAnalysisResult] = None
        self._reviews: List[Review] = []
        
        self._events: List[DomainEvent] = []
        self._events.append(ComplaintCreated(c_id.value, news_url.url))

    @property
    def id(self) -> str: return self._id.value
    
    @property
    def status(self) -> str: return self._status

    @property
    def events(self) -> List[DomainEvent]: return self._events

    def clear_events(self):
        self._events.clear()

    # ИНВАРИАНТ 1: Прикрепление результата ИИ
    def attach_ai_analysis(self, result: AIAnalysisResult):
        if self._status != "PENDING":
            raise InvalidComplaintStatusException("ИИ анализ можно добавить только в статусе PENDING")
        
        self._ai_result = result
        self._events.append(AIAnalysisAttached(self.id, result.fake_probability_score))
        
        # Бизнес-правило: Если ИИ уверен на 95%+, сразу блокируем новость
        if result.fake_probability_score >= self.AUTO_BLOCK_THRESHOLD:
            self.confirm_as_fake("Автоматическая блокировка нейросетью")
        else:
            self._status = "IN_REVIEW"  # Требуется проверка человеком

    # ИНВАРИАНТ 2: Добавление ревью от модератора
    def add_human_review(self, review: Review):
        if self._status not in ["PENDING", "IN_REVIEW"]:
            raise InvalidComplaintStatusException(f"Нельзя добавить проверку в статусе {self._status}")
        
        # Проверка на дубликаты модераторов
        if any(r.moderator_id == review.moderator_id for r in self._reviews):
            raise RuleViolationException("Этот модератор уже проверил данную жалобу")
            
        self._reviews.append(review)

    # ИНВАРИАНТ 3: Подтверждение фейка
    def confirm_as_fake(self, final_reason: str):
        if self._status in ["FAKE_CONFIRMED", "REJECTED"]:
            raise InvalidComplaintStatusException("Жалоба уже обработана")
            
        # Защита: нельзя подтвердить без уверенности ИИ или без живого ревью
        has_high_ai = self._ai_result and self._ai_result.fake_probability_score >= self.AUTO_BLOCK_THRESHOLD
        has_fake_reviews = any(r.is_fake for r in self._reviews)
        
        if not (has_high_ai or has_fake_reviews):
            raise RuleViolationException("Нельзя заблокировать новость без подтверждения модератором или высокого скора ИИ")
            
        self._status = "FAKE_CONFIRMED"
        self._events.append(ComplaintClosedAsFake(self.id, final_reason))