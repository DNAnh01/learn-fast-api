import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr
from sqlalchemy import Boolean, Column, DateTime, String
from sqlalchemy.dialects.postgresql.base import UUID


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserLogin(UserBase):
    password: str


class UserOut(UserBase):
    id: uuid.UUID
    created_at: datetime

    class Config:
        orm_mode = True


class UserInDB:
    id: uuid.UUID
    email: String
    password: String
    display_name: String
    avatar_url: String
    created_at: DateTime
    updated_at: DateTime
    user_role: String
    is_verified: Boolean
    is_active: Boolean
    deleted_at: Optional[DateTime]


class UserUpdate(UserBase):
    password: Optional[str] = None
    display_name: Optional[str] = None
    avatar_url: Optional[str] = None
    is_verified: Optional[bool] = None
    user_role: Optional[str] = None
