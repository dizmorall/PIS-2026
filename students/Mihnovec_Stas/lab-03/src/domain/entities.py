from datetime import datetime
from .exceptions import RuleViolationException

class Moderator:
    """Entity 1: Модератор (самостоятельная сущность)"""
    def __init__(self, mod_id: str, name: str):
        self.id = mod_id
        self.name = name
        self.reputation = 100

    def decrease_reputation(self, penalty: int):
        self.reputation -= penalty

class Review:
    """Entity 2: Оценка модератора (живет внутри агрегата Complaint)"""
    def __init__(self, review_id: str, moderator_id: str, is_fake: bool, comment: str):
        if not comment:
            raise RuleViolationException("Комментарий проверки не может быть пустым")
        
        self.id = review_id
        self.moderator_id = moderator_id
        self.is_fake = is_fake
        self.comment = comment
        self.created_at = datetime.now()

    def __eq__(self, other):
        if not isinstance(other, Review): return False
        return self.id == other.id