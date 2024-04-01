import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


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


class UserUpdate(UserBase):
    password: Optional[str] = None
    display_name: Optional[str] = None
    avatar_url: Optional[str] = None
    user_role: Optional[str] = None
