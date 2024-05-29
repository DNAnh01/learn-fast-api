from datetime import datetime, timedelta

from sqlalchemy import Column, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql.base import UUID
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class UserSubscription(Base):
    __tablename__ = "user_subscriptions"
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"))
    plan_id = Column(
        UUID(as_uuid=True), ForeignKey("subscription_plans.id", ondelete="CASCADE")
    )
    expire_at = Column(
        DateTime(timezone=True), default=datetime.now() + timedelta(days=30)
    )

    user = relationship("User", back_populates="subscriptions")
    plan = relationship("SubscriptionPlan", back_populates="user_subscriptions")
