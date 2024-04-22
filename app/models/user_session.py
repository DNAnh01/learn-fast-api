from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql.base import UUID
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class UserSession(Base):
    __tablename__ = "user_sessions"
    token = Column(String, unique=True, nullable=False)
    expires_at = Column(DateTime(timezone=True), default=datetime.now, nullable=False)

    user_id = Column(
        UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )


    user = relationship("User", back_populates="sessions")
