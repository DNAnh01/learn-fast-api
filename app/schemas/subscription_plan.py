import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class SubscriptionPlanBase(BaseModel):
    plan_title: str
    plan_price: float
    available_model: str
    message_credits: int
    number_of_chatbots: int
    max_character_per_chatbot: int
    live_agent_takeover: bool
    remove_label: bool

    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    is_active: Optional[bool]
    deleted_at: Optional[datetime]


class SubscriptionPlanCreate(SubscriptionPlanBase):
    pass


class SubscriptionPlanOut(BaseModel):
    id: uuid.UUID
    plan_title: str
    plan_price: float
    available_model: str
    message_credits: int
    number_of_chatbots: int
    max_character_per_chatbot: int
    live_agent_takeover: bool
    remove_label: bool

    is_active: bool
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime]

    class Config:
        orm_mode = True


class SubscriptionPlanUpdate(BaseModel):
    plan_title: Optional[str]
    plan_price: Optional[float]
    available_model: Optional[str]
    message_credits: Optional[int]
    number_of_chatbots: Optional[int]
    max_character_per_chatbot: Optional[int]
    live_agent_takeover: Optional[bool]
    remove_label: Optional[bool]

    updated_at: Optional[datetime]
