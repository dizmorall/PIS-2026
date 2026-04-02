# Заглушки портов (в проекте импортируются из портов Лабы 2)
class EventPublisher:
    def publish(self, events): pass

from .commands import CreateComplaintCommand, AddHumanReviewCommand
# from src.domain.aggregate import Complaint
# from src.domain.value_objects import ComplaintId, NewsUrl, Reason
# from src.domain.entities import Review

class CreateComplaintHandler:
    """Обработчик создания жалобы"""
    
    def __init__(self, repository, event_publisher: EventPublisher):
        self.repository = repository
        self.event_publisher = event_publisher

    def handle(self, command: CreateComplaintCommand) -> str:
        # 1. Трансформируем примитивы в Value Objects (Lab 3)
        # c_id = ComplaintId(command.complaint_id)
        # url = NewsUrl(command.news_url)
        # reason = Reason(command.reason_category, command.reason_details)
        
        # 2. Создаем агрегат (вызов бизнес-логики)
        # complaint = Complaint(c_id, url, command.reporter_id, reason)
        
        # 3. Сохраняем в БД
        # self.repository.save(complaint)
        
        # 4. Публикуем доменные события (например, для уведомлений)
        # self.event_publisher.publish(complaint.events)
        # complaint.clear_events()
        
        return command.complaint_id

class AddHumanReviewHandler:
    """Обработчик добавления ревью модератором"""
    
    def __init__(self, repository, event_publisher: EventPublisher):
        self.repository = repository
        self.event_publisher = event_publisher

    def handle(self, command: AddHumanReviewCommand) -> None:
        # 1. Загружаем агрегат
        # complaint = self.repository.find_by_id(command.complaint_id)
        # if not complaint: raise Exception("Жалоба не найдена")
        
        # 2. Вызываем доменный метод (сработают инварианты)
        # review = Review("REV-1", command.moderator_id, command.is_fake, command.comment)
        # complaint.add_human_review(review)
        
        # 3. Сохраняем изменения и публикуем события
        # self.repository.save(complaint)
        # self.event_publisher.publish(complaint.events)
        # complaint.clear_events()
        pass