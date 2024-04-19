from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql.base import UUID
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.models.conversation import Conversation


class ChatBot(Base):
    __tablename__ = "chatbots"
    chatbot_name = Column(String, nullable=False)
    model = Column(String, nullable=False)
    description = Column(String)
    temperature = Column(Float, default=0.5)
    max_tokens = Column(Integer, default=100)
    is_default = Column(Boolean, default=True)
    prompt = Column(
        String,
        default="You are a helpful assistant. The first prompt will be a long text,"
        "and any messages that you get be regarding that. Please answer any "
        "questions and requests having in mind the first prompt ",
    )
    user_id = Column(
        UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )

    conversations = relationship("Conversation", back_populates="chatbot")
    user = relationship("User", back_populates="chatbots")