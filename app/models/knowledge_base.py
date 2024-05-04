import uuid

from sqlalchemy import Boolean, Column, String, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql.base import UUID

from app.db.base_class import Base


class KnowledgeBase(Base):
<<<<<<< HEAD
    __tablename__ = "knowledge_base"
=======
    __tablename__ = "knowledgebase"
>>>>>>> origin/feature/MessageAndConversation
    title = Column(String, nullable=False)
    content_type = Column(String, nullable=False)
    file_path = Column(String)
    character_count = Column(Integer)
    file_size = Column(Float)
    chatbot_id = Column(UUID(as_uuid=True), ForeignKey("chatbots.id", ondelete="CASCADE"), nullable=False)
<<<<<<< HEAD
    chatbot = relationship("ChatBot", back_populates="knowledge_base")
=======
    chatbot = relationship("ChatBot", back_populates="knowledgebase")
>>>>>>> origin/feature/MessageAndConversation

