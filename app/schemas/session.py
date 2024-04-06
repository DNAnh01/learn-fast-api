import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class SessionBase(BaseModel):
    token: str
    expires_at: Optional[datetime]


class SessionCreate(SessionBase):
    user_id: uuid.UUID


class SessionOut(SessionBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime]

    class Config:
        orm_mode = True


class SessionUpdate(SessionBase):
    token: Optional[str] = None
    expires_at: Optional[datetime] = None
