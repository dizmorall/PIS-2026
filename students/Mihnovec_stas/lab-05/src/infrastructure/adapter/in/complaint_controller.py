from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
# Импорты команд и фасада из Lab 4
from src.application.command.commands import CreateComplaintCommand, AddHumanReviewCommand
from src.application.query.queries import GetComplaintByIdQuery

router = APIRouter(prefix="/api/complaints", tags=["Complaints"])

# --- Pydantic модели для HTTP запросов (HTTP DTOs) ---
class CreateComplaintRequest(BaseModel):
    news_url: str
    reporter_id: str
    reason_category: str
    reason_details: str

class AddReviewRequest(BaseModel):
    moderator_id: str
    is_fake: bool
    comment: str

# --- REST Эндпоинты ---

@router.post("/", status_code=201)
def create_complaint(request: CreateComplaintRequest, facade = Depends(get_facade)): # type: ignore
    """REST API: Создать жалобу (Вызывает Command)"""
    import uuid
    command = CreateComplaintCommand(
        complaint_id=f"CMP-{uuid.uuid4().hex[:6]}",
        news_url=request.news_url,
        reporter_id=request.reporter_id,
        reason_category=request.reason_category,
        reason_details=request.reason_details
    )
    complaint_id = facade.create_complaint(command)
    return {"id": complaint_id, "message": "Жалоба создана"}

@router.post("/{complaint_id}/review")
def add_human_review(complaint_id: str, request: AddReviewRequest, facade = Depends(get_facade)): # type: ignore
    """REST API: Добавить проверку модератором (Вызывает Command)"""
    command = AddHumanReviewCommand(
        complaint_id=complaint_id,
        moderator_id=request.moderator_id,
        is_fake=request.is_fake,
        comment=request.comment
    )
    facade.add_human_review(command)
    return {"message": "Ревью успешно добавлено"}

@router.get("/{complaint_id}")
def get_complaint(complaint_id: str, facade = Depends(get_facade)): # type: ignore
    """REST API: Получить жалобу (Вызывает Query)"""
    query = GetComplaintByIdQuery(complaint_id=complaint_id)
    result_dto = facade.get_complaint_by_id(query)
    
    if not result_dto:
        raise HTTPException(status_code=404, detail="Жалоба не найдена")
    return result_dto