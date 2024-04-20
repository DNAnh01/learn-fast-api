import uuid

from sqlalchemy import Boolean, Column, String, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql.base import UUID

from app.db.base_class import Base


class KnowledgeBase(Base):
    __tablename__ = "knowledgebase"
    title = Column(String, nullable=False)
    content_type = Column(String, nullable=False)
    file_path = Column(String)
    character_count = Column(Integer)
    file_size = Column(Float)
    chatbot_id = Column(UUID(as_uuid=True), ForeignKey("chatbots.id", ondelete="CASCADE"), nullable=False)
    chatbot = relationship("ChatBot", back_populates="knowledgebase")

