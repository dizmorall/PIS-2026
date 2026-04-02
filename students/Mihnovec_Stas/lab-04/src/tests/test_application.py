import pytest
from src.application.command.commands import CreateComplaintCommand
from src.application.command.handlers import CreateComplaintHandler
from src.application.query.queries import GetComplaintByIdQuery
from src.application.query.handlers import GetComplaintByIdHandler

class MockRepo:
    def save(self, obj): pass
    def find_by_id(self, id): return None

class MockEventPublisher:
    def publish(self, events): pass

def test_create_complaint_handler_validates_basic_rules():
    with pytest.raises(ValueError, match="ID и URL обязательны"):
        CreateComplaintCommand("", "", "user_1", "FAKE_NEWS", "Детали")

def test_handler_executes_successfully():
    repo = MockRepo()
    publisher = MockEventPublisher()
    handler = CreateComplaintHandler(repo, publisher)
    
    cmd = CreateComplaintCommand("CMP-99", "http://test.com", "user_1", "SCAM", "1234567890")
    
    # Хендлер должен вернуть ID (имитация успешной работы)
    result_id = handler.handle(cmd)
    assert result_id == "CMP-99"

def test_query_handler_returns_dto():
    repo = MockRepo()
    handler = GetComplaintByIdHandler(repo)
    
    query = GetComplaintByIdQuery("CMP-1")
    dto = handler.handle(query)
    
    assert dto.id == "CMP-1"
    assert dto.status == "PENDING"