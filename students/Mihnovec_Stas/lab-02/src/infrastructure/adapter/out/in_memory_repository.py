from application.port.out.complaint_repository import ComplaintRepository
from domain.models.complaint import Complaint

class InMemoryComplaintRepository(ComplaintRepository):
    """Реализация порта репозитория (хранение в оперативной памяти)"""
    
    def __init__(self):
        self._db = {}
    
    def save(self, complaint: Complaint) -> None:
        self._db[complaint.id] = complaint
        print(f"[DB] Жалоба {complaint.id} сохранена в память.")
    
    def find_by_id(self, complaint_id: str) -> Complaint:
        return self._db.get(complaint_id)