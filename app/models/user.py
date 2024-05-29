from sqlalchemy import Boolean, Column, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.models.chatbot import ChatBot
from app.models.conversation import Conversation
from app.models.user_session import UserSession
from app.models.user_subscription import UserSubscription


class User(Base):
    __tablename__ = "users"
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    display_name = Column(String, nullable=False, default="user")
    avatar_url = Column(
        String,
        nullable=False,
        default="http://localhost:3000/Ellipse%201.svg",
    )
    payment_information = Column(String, nullable=True)
    is_verified = Column(Boolean, default=False, nullable=False)
    user_role = Column(String, nullable=False, default="user")
    
    sessions = relationship("UserSession", back_populates="user")
    subscriptions = relationship("UserSubscription", back_populates="user")
    chatbots = relationship("ChatBot", back_populates="user")
    conversations = relationship("Conversation", back_populates="user")