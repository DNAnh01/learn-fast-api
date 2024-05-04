import uuid
from typing import Optional

from pydantic import BaseModel


class ChatBotBase(BaseModel):
    user_id: uuid.UUID


class ChatBotCreate(BaseModel):
    chatbot_name: str
    model: str
    description: str
    temperature: float
    max_tokens: int
    is_default: bool
    prompt: str

<<<<<<< HEAD

=======
>>>>>>> origin/feature/MessageAndConversation
class ChatBotUpdate(ChatBotBase):
    chatbot_name: Optional[str] = None
    model: Optional[str] = None
    description: Optional[str] = None
    temperature: Optional[float] = None
    max_tokens: Optional[int] = None
    is_default: Optional[bool] = None
    prompt: Optional[str] = None
<<<<<<< HEAD
=======
    chatbot_config: Optional[dict] = None
>>>>>>> origin/feature/MessageAndConversation


class ChatBotOut(ChatBotBase):
    id: uuid.UUID
    chatbot_name: str
    model: str
    description: str
    temperature: float
    max_tokens: int
    is_default: bool
    prompt: str
<<<<<<< HEAD
=======
    chatbot_config: dict
>>>>>>> origin/feature/MessageAndConversation

    class Config:
        orm_mode = True


class ChatBotInDB(ChatBotBase):
    chatbot_name: str
    model: str
    description: str
    temperature: float
    max_tokens: int
    is_default: bool
    prompt: str

    class Config:
        orm_mode = True
