from datetime import datetime
from typing import List

from pydantic import UUID4, BaseModel

from app.common.string_case import to_camel_case


class UserBase(BaseModel):

    full_name: str

    class Config:
        alias_generator = to_camel_case
        populate_by_name = True


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class UserInDBBase(UserBase):
    id: UUID4
    created_at: datetime
    updated_at: datetime
    is_active: bool

    class Config:
        from_attributes = True


class User(UserInDBBase):
    pass


class Users(BaseModel):
    total: int
    results: List[User]
