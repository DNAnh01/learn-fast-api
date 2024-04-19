from sqlalchemy import Column, DateTime, Float, ForeignKey
from sqlalchemy.dialects.postgresql.base import UUID
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.models.message import Message


class Conversation(Base):
    __tablename__ = "conversations"
    chatbot_id = Column(UUID(as_uuid=True), ForeignKey("chatbots.id"), nullable=False)

    user_id = Column(
        UUID(as_uuid=True), ForeignKey('users.id', ondelete="CASCADE"), nullable=True
    )

    started_at = Column(DateTime)
    ended_at = Column(DateTime)
    rating_score = Column(Float, nullable=True)


    user = relationship("User", back_populates="conversations")

    chatbot = relationship("ChatBot", back_populates="conversations")

    # conversation 1-n messages

    messages = relationship("Message", back_populates="conversation")
