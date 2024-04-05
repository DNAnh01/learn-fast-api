from sqlalchemy import Boolean, Column, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class User(Base):
    __tablename__ = "users"
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    display_name = Column(String)
    avatar_url = Column(String)
    is_verified = Column(Boolean, default=False)
    user_role = Column(String)

    sessions = relationship("Session", back_populates="user")
