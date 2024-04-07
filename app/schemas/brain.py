import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from sqlalchemy import Boolean, Column, DateTime, String
from sqlalchemy.dialects.postgresql.base import UUID


class BrainBase(BaseModel):
    user_id: uuid.UUID


class BrainCreate(BrainBase):
    brain_name: str
    model: str
    description: str
    temperature: float
    max_tokens: int
    is_default: bool
    prompt: str

class BrainUpdate(BrainBase):
    brain_name: Optional[str] = None
    model: Optional[str] = None
    description: Optional[str] = None
    temperature: Optional[float] = None
    max_tokens: Optional[int] = None
    is_default: Optional[bool] = None
    prompt: Optional[str] = None

class BrainOut(BrainBase):
    brain_name: str
    model: str
    description: str
    temperature: float
    max_tokens: int
    is_default: bool
    prompt: str

    class Config:
        orm_mode = True

#
# class BrainInDB:
#     id: uuid.UUID
#     email: String
#     password: String
#     display_name: String
#     avatar_url: String
#     created_at: DateTime
#     updated_at: DateTime
#     user_role: String
#     is_verified: Boolean
#     is_active: Boolean
#     deleted_at: Optional[DateTime]
#
