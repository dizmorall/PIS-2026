from sqlalchemy.orm import Session
from src.infrastructure.orm.models import ComplaintModel, ReviewModel
# from src.domain.aggregate import Complaint (Импорт из Lab 3)
# from src.application.port.out.complaint_repository import ComplaintRepository (Импорт из Lab 2)

class PostgresComplaintRepository: # Наследует ComplaintRepository
    """Адаптер для работы с PostgreSQL через SQLAlchemy"""
    
    def __init__(self, db_session: Session):
        self.db = db_session

    def save(self, complaint) -> None:
        """Сохраняет или обновляет агрегат в БД"""
        # 1. Маппинг Домена в ORM
        db_complaint = ComplaintModel(
            id=complaint.id,
            news_url=complaint._news_url.url,
            reporter_id=complaint._reporter_id,
            reason_category=complaint._reason.category,
            reason_details=complaint._reason.details,
            status=complaint.status,
            ai_score=complaint._ai_result.fake_probability_score if complaint._ai_result else None
        )
        
        # Маппинг вложенных сущностей (Reviews)
        db_complaint.reviews = [
            ReviewModel(
                id=r.id, 
                moderator_id=r.moderator_id, 
                is_fake=r.is_fake, 
                comment=r.comment
            ) for r in complaint._reviews
        ]

        # 2. Сохранение (merge обновляет существующие и вставляет новые)
        self.db.merge(db_complaint)
        self.db.commit()

    def find_by_id(self, complaint_id: str):
        """Загружает агрегат из БД"""
        db_model = self.db.query(ComplaintModel).filter(ComplaintModel.id == complaint_id).first()
        if not db_model:
            return None
        
        # TODO: Здесь должен быть обратный маппинг из ORM ComplaintModel в Domain Complaint
        # return map_to_domain(db_model)
        pass