import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class SessionBase(BaseModel):
    token: str
    expires_at: datetime

    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    is_active: Optional[bool]
    deleted_at: Optional[datetime]



class SessionCreate(SessionBase):
    user_id: uuid.UUID



class SessionOut(BaseModel):
    id: uuid.UUID
    token: str
    expires_at: datetime

    user_id: uuid.UUID

    is_active: bool
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime]

    class Config:
        orm_mode = True


class SessionInDB(BaseModel):
    id: uuid.UUID
    token: str
    expires_at: datetime

    user_id: uuid.UUID

    is_active: bool
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime]


class SessionUpdate(BaseModel):
    token: Optional[str]
    expires_at: Optional[datetime]

    updated_at: Optional[datetime]
