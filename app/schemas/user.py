import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    deleted_at: Optional[datetime] = None


class UserSignUp(BaseModel):
    email: EmailStr
    password: str


class UserCreate(UserBase):
    password_hash: str


class UserSignIn(BaseModel):
    email: EmailStr
    password: str


class UserSignInWithGoogle(UserBase):
    password_hash: Optional[str]
    display_name: Optional[str]
    avatar_url: Optional[str]
    is_verified: Optional[bool]
    user_role: Optional[str]


class UserUpdate(UserBase):
    password_hash: Optional[str]
    display_name: Optional[str]
    avatar_url: Optional[str]
    is_verified: Optional[bool]
    user_role: Optional[str]

    updated_at: Optional[datetime]


class UserOut(BaseModel):
    id: uuid.UUID
    email: EmailStr
    display_name: str
    avatar_url: str
    payment_information: Optional[str]
    is_verified: bool
    user_role: str
    is_active: bool
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime]

    class Config:
        orm_mode = True


class UserInDB(BaseModel):
    id: uuid.UUID
    email: EmailStr
    password_hash: str
    display_name: str
    avatar_url: str
    payment_information: Optional[str]
    is_verified: bool
    user_role: str

    is_active: bool
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime]
