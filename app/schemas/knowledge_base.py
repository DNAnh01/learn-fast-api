import uuid
from typing import Optional

from pydantic import BaseModel


class KnowledgeBaseBase(BaseModel):
    chatbot_id: uuid.UUID


class KnowledgeBaseAdd(BaseModel):
    title: str
    content_type: str
    file_path: str
    character_count: float
    file_size: int


class KnowledgeBaseRemove(BaseModel):
    id: uuid.UUID




class KnowledgeBaseOut(KnowledgeBaseBase):
    id: uuid.UUID
    title: str
    content_type: str
    file_path: str
    character_count: float
    file_size: int

    class Config:
        orm_mode = True


class KnowledgeBaseInDB(KnowledgeBaseBase):
    title: str
    content_type: str
    file_path: str
    character_count: float
    file_size: int

    class Config:
        orm_mode = True
