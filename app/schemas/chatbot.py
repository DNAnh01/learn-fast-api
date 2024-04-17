import uuid
from typing import Optional

from pydantic import BaseModel


class ChatBotBase(BaseModel):
    user_id: uuid.UUID


class ChatBotCreate(ChatBotBase):
    chatbot_name: str
    model: str
    description: str
    temperature: float
    max_tokens: int
    is_default: bool
    prompt: str


class ChatBotUpdate(ChatBotBase):
    chatbot_name: Optional[str] = None
    model: Optional[str] = None
    description: Optional[str] = None
    temperature: Optional[float] = None
    max_tokens: Optional[int] = None
    is_default: Optional[bool] = None
    prompt: Optional[str] = None


class ChatBotOut(ChatBotBase):
    chatbot_name: str
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
