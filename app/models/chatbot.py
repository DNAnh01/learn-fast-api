from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String, JSON
from sqlalchemy.dialects.postgresql.base import UUID
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.models.conversation import Conversation
from app.models.knowledge_base import KnowledgeBase


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
    chatbot_config = Column(JSON, default={
        "font_family": "Default",
        "font_size": 14,
        "input_background": "#FFFFFF",
        "background_color": "#FFFFFF",
        "user_font_color": "#FFFFFF",
        "prompts_font_color": "#272727",
        "ally_font_color": "#272727",
        "disclaimer_color": "#676767",
        "input_placeholder": "Write your message",
        "disclaimer_text": "",
        "chatbot_logo": "https://i.imgur.com/KWvPAWC.png",
        "website_link": "https://ally.com",
        "powered_by_remove": 0
    })
    user_id = Column(
        UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    knowledgebase = relationship("KnowledgeBase", back_populates="chatbot")
    conversations = relationship("Conversation", back_populates="chatbot")
    user = relationship("User", back_populates="chatbots")