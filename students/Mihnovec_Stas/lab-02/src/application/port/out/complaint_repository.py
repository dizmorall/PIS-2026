from abc import ABC, abstractmethod
from domain.models.complaint import Complaint

class ComplaintRepository(ABC):
    """Исходящий порт: сохранение и загрузка жалоб"""
    
    @abstractmethod
    def save(self, complaint: Complaint) -> None:
        pass
    
    @abstractmethod
    def find_by_id(self, complaint_id: str) -> Complaint:
        pass