from sqlalchemy import Boolean, Column, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class User(Base):
    __tablename__ = "users"
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    display_name = Column(String, nullable=False, default="user")
    avatar_url = Column(
        String,
        nullable=False,
        default="https://raw.githubusercontent.com/DNAnh01/assets/main/default_user_avatar.png",
    )
    payment_information = Column(String, nullable=True)
    is_verified = Column(Boolean, default=False, nullable=False)
    user_role = Column(String, nullable=False, default="user")
    chatbots = relationship("ChatBot", back_populates="user")
    sessions = relationship("Session", back_populates="user")
    subscriptions = relationship("UserSubscription", back_populates="user")
