# from src.cqrs.read_model.complaint_view import ComplaintDashboardView, ComplaintViewRepository
from datetime import datetime

class ComplaintProjection:
    """
    Проектор: слушает доменные события и обновляет Read Model.
    Обеспечивает Eventual Consistency (согласованность в конечном счете).
    """
    
    def __init__(self, view_repository): # type: ignore
        self.view_repo = view_repository

    def handle_complaint_created(self, event):
        """Создает базовую плоскую запись при создании жалобы"""
        view = ComplaintDashboardView( # type: ignore
            id=event.complaint_id,
            news_url=event.news_url,
            status="PENDING",
            total_reviews_count=0,
            fake_votes_count=0,
            last_updated_at=datetime.now().isoformat()
        )
        self.view_repo.save_view(view)

    def handle_review_added(self, event):
        """
        Инкрементальное обновление!
        Вместо пересчета JOIN-ов, мы просто прибавляем +1 к счетчикам.
        """
        view = self.view_repo.get_by_id(event.complaint_id)
        if view:
            view.total_reviews_count += 1
            if event.is_fake:
                view.fake_votes_count += 1
            view.last_updated_at = datetime.now().isoformat()
            self.view_repo.save_view(view)