from abc import ABC, abstractmethod

class CreateComplaintCommand:
    """DTO для команды создания жалобы"""
    def __init__(self, user_id: str, news_id: str, reason: str, news_text: str):
        self.user_id = user_id
        self.news_id = news_id
        self.reason = reason
        self.news_text = news_text

class CreateComplaintUseCase(ABC):
    """Входящий порт: подача жалобы на новость"""
    
    @abstractmethod
    def create_complaint(self, command: CreateComplaintCommand) -> str:
        """
        Создаёт жалобу, отправляет на проверку ИИ и сохраняет в БД.
        :param command: Данные жалобы
        :return: ID созданной жалобы
        """
        pass