from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from uuid import UUID


class MessageBase(BaseModel):
    message: str
    sent_at: datetime


class MessageCreate(MessageBase):
    sender_id: UUID
    sender_type: str
    conversation_id: UUID


class MessageOut(MessageBase):
    id: UUID
    conversation_id: UUID
    message: str
    sender_id: UUID
    sender_type: str
    sent_at: datetime

    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


class MessageCollectionOut(BaseModel):
    messages: List[MessageOut]


class MessageUpdate(BaseModel):
    message: Optional[str] = None
    updated_at: datetime
