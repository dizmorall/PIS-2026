# src/application/query/handlers.py
from .dtos import ComplaintDto
from .queries import GetComplaintByIdQuery

class GetComplaintByIdHandler:
    def __init__(self, repository):
        self.repository = repository

    def handle(self, query: GetComplaintByIdQuery) -> ComplaintDto:
        # complaint = self.repository.find_by_id(query.complaint_id)
        # if not complaint: return None
        
        # Маппинг Доменной модели в Read DTO
        # return ComplaintDto(
        #     id=complaint.id,
        #     url=complaint._news_url.url,
        #     status=complaint.status,
        #     ai_score=complaint._ai_result.fake_probability_score if complaint._ai_result else 0,
        #     reviews_count=len(complaint._reviews)
        # )
        return ComplaintDto("CMP-1", "http://news.com", "PENDING", 0, 0)