from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.infrastructure.config.database import Base

class ComplaintModel(Base):
    __tablename__ = "complaints"

    id = Column(String, primary_key=True, index=True)
    news_url = Column(String, nullable=False)
    reporter_id = Column(String, nullable=False)
    reason_category = Column(String, nullable=False)
    reason_details = Column(String, nullable=False)
    status = Column(String, nullable=False, default="PENDING")
    ai_score = Column(Integer, nullable=True)

    # Отношение один-ко-многим для проверок модераторами
    reviews = relationship("ReviewModel", back_populates="complaint", cascade="all, delete-orphan")


class ReviewModel(Base):
    __tablename__ = "reviews"

    id = Column(String, primary_key=True)
    complaint_id = Column(String, ForeignKey("complaints.id"))
    moderator_id = Column(String, nullable=False)
    is_fake = Column(Boolean, nullable=False)
    comment = Column(String, nullable=False)

    complaint = relationship("ComplaintModel", back_populates="reviews")