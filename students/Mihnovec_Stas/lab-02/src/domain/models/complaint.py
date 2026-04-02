import uuid
from datetime import datetime

class Complaint:
    """Доменная модель: Жалоба на новость"""
    
    def __init__(self, user_id: str, news_id: str, reason: str):
        self.id = str(uuid.uuid4())
        self.user_id = user_id
        self.news_id = news_id
        self.reason = reason
        self.status = "PENDING"
        self.created_at = datetime.now()
    
    def mark_as_review_pending(self):
        """Изменить статус после ответа от ИИ"""
        self.status = "REVIEW_PENDING"

    def reject(self):
        self.status = "REJECTED"