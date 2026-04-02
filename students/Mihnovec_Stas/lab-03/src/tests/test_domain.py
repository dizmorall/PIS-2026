import pytest
from src.domain.value_objects import ComplaintId, NewsUrl, Reason, AIAnalysisResult
from src.domain.entities import Review
from src.domain.aggregate import Complaint
from src.domain.exceptions import RuleViolationException, InvalidComplaintStatusException
from src.domain.events import ComplaintClosedAsFake

def test_should_not_create_invalid_news_url():
    with pytest.raises(RuleViolationException):
        NewsUrl("ftp://bad-url.com")

def test_should_not_create_invalid_reason():
    with pytest.raises(RuleViolationException):
        Reason("WRONG_CATEGORY", "Слишком коротко")

def test_auto_block_if_ai_score_is_high():
    complaint = Complaint(
        ComplaintId("CMP-01"), 
        NewsUrl("https://news.com/1"), 
        "user_1", 
        Reason("FAKE_NEWS", "Полный бред и выдумка")
    )
    
    complaint.attach_ai_analysis(AIAnalysisResult(99, tuple()))
    
    assert complaint.status == "FAKE_CONFIRMED"
    assert any(isinstance(e, ComplaintClosedAsFake) for e in complaint.events)

def test_cannot_confirm_fake_without_evidence():
    complaint = Complaint(
        ComplaintId("CMP-02"), 
        NewsUrl("https://news.com/2"), 
        "user_1", 
        Reason("SCAM", "Подозрительная ссылка")
    )
    # ИИ не уверен (скор 50)
    complaint.attach_ai_analysis(AIAnalysisResult(50, tuple()))
    
    with pytest.raises(RuleViolationException):
        complaint.confirm_as_fake("Мне так кажется")

def test_cannot_add_review_to_closed_complaint():
    complaint = Complaint(
        ComplaintId("CMP-03"), 
        NewsUrl("https://news.com/3"), 
        "user_1", 
        Reason("OTHER", "Оскорбления в тексте")
    )
    complaint.attach_ai_analysis(AIAnalysisResult(99, tuple())) # Авто-закрытие
    
    with pytest.raises(InvalidComplaintStatusException):
        complaint.add_human_review(Review("REV-1", "mod_1", True, "Точно фейк"))