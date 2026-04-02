from infrastructure.adapter.out.in_memory_repository import InMemoryComplaintRepository

class DummyAIAdapter:
    def analyze_text(self, text): return "REQUIRES_REVIEW"

from application.service.complaint_service import ComplaintService

class DependencyContainer:
    """Конфигурация DI: связывание портов и адаптеров"""
    
    def __init__(self):
        self.complaint_repository = InMemoryComplaintRepository()
        self.ai_adapter = DummyAIAdapter()
        
        self.complaint_service = ComplaintService(
            repository=self.complaint_repository,
            ai_moderation=self.ai_adapter
        )
    
    def get_complaint_service(self) -> ComplaintService:
        return self.complaint_service