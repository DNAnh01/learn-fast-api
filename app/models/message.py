# "conversational.py"
from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql.base import UUID
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Message(Base):
    __tablename__ = "messages"
    conversation_id = Column(
        UUID(as_uuid=True), ForeignKey("conversations.id", ondelete="CASCADE"), nullable=False
    )
    sender_id = Column(String)
    sender_type = Column(String)  # user or bot
    message = Column(String)

    conversation = relationship("Conversation", back_populates="messages")
