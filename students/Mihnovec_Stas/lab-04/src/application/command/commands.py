from dataclasses import dataclass

@dataclass(frozen=True)
class CreateComplaintCommand:
    """Команда: Создать новую жалобу"""
    complaint_id: str
    news_url: str
    reporter_id: str
    reason_category: str
    reason_details: str
    
    def __post_init__(self):
        if not self.complaint_id or not self.news_url:
            raise ValueError("ID и URL обязательны")

@dataclass(frozen=True)
class AddHumanReviewCommand:
    """Команда: Добавить проверку модератором"""
    complaint_id: str
    moderator_id: str
    is_fake: bool
    comment: str

    def __post_init__(self):
        if not self.complaint_id or not self.moderator_id:
            raise ValueError("ID жалобы и модератора обязательны")