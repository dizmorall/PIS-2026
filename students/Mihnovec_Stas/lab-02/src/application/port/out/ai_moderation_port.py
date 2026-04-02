from abc import ABC, abstractmethod

class AIModerationPort(ABC):
    """Исходящий порт: проверка текста новости через ИИ"""
    
    @abstractmethod
    def analyze_text(self, text: str) -> str:
        """
        Отправляет текст на анализ
        :return: Статус (например, 'REQUIRES_REVIEW', 'FAKE_CONFIRMED')
        """
        pass