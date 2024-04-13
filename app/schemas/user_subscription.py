import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class UserSubscriptionBase(BaseModel):
    user_id: uuid.UUID
    plan_id: uuid.UUID
    expire_at: Optional[datetime]

    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    is_active: Optional[bool]
    deleted_at: Optional[datetime]


class UserSubscriptionCreate(UserSubscriptionBase):
    pass


class UserSubscriptionOut(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    plan_id: uuid.UUID
    expire_at: datetime

    is_active: bool
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime]

    class Config:
        orm_mode = True


class UserSubscriptionUpdate(BaseModel):
    user_id: Optional[uuid.UUID]
    plan_id: Optional[uuid.UUID]
    expire_at: Optional[datetime]

    updated_at: Optional[datetime]
