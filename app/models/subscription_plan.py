from sqlalchemy import Boolean, Column, Float, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class SubscriptionPlan(Base):
    __tablename__ = "subscription_plans"
    plan_title = Column(String, nullable=False, default="monthly_free")
    plan_price = Column(Float, nullable=False, default=0.0)
    available_model = Column(String, nullable=False, default="GPT-3.5-Turbo LLM")
    message_credits = Column(Integer, nullable=False, default=30)
    number_of_chatbots = Column(Integer, nullable=False, default=1)
    max_character_per_chatbot = Column(Integer, nullable=False, default=200000)
    live_agent_takeover = Column(Boolean, nullable=False, default=False)
    remove_label = Column(Boolean, nullable=False, default=False)

    user_subscriptions = relationship("UserSubscription", back_populates="plan")
