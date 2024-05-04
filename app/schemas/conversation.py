from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import UUID


class ConversationBase(BaseModel):
<<<<<<< HEAD
    started_at: datetime
=======
    # started_at: datetime
>>>>>>> origin/feature/MessageAndConversation
    ended_at: datetime
    rating_score: Optional[float] = None


class ConversationCreate(ConversationBase):
    user_id: UUID
    chatbot_id: UUID


class ConversationOut(ConversationBase):
    id: UUID
    user_id: UUID
    chatbot_id: UUID
<<<<<<< HEAD
    started_at: datetime
    ended_at: datetime
    rating_score: Optional[float]
    conversation_name: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
=======
    # started_at: datetime
    conversation_name: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    ended_at: Optional[datetime]
    rating_score: Optional[float]
    is_taken: bool
>>>>>>> origin/feature/MessageAndConversation

    class Config:
        orm_mode = True


class ConversationUpdate(BaseModel):
    ended_at: datetime
    rating_score: Optional[float] = None
    updated_at: datetime
