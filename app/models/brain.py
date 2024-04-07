from sqlalchemy import Boolean, Column, String, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql.base import UUID

from app.db.base_class import Base


class Brain(Base):
    __tablename__ = "brains"
    brain_name = Column(String, nullable=False)
    model = Column(String, nullable=False)
    description = Column(String)
    temperature = Column(Float, default=0.5)
    max_tokens = Column(Integer, default=100)
    is_default = Column(Boolean, default=True)
    prompt = Column(String, default='You are a helpful assistant. The first prompt will be a long text,'
                                        'and any messages that you get be regarding that. Please answer any '
                                        'questions and requests having in mind the first prompt ')
    user_id = Column(
        UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )

    user = relationship("User", back_populates="brains")
