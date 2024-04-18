from abc import ABC, abstractmethod
from typing import Optional
from app.schemas.message import MessageCreate, MessageUpdate, MessageOut, MessageCollectionOut
from sqlalchemy.orm import Session

from uuid import UUID


class MessageService(ABC):
    @abstractmethod
    def create(self, db: Session, message: MessageCreate, token: str) -> MessageOut:
        pass

    @abstractmethod
    def get_messages_by_conversation_id(self, db: Session, conversation_id: str, token: str) -> MessageCollectionOut:
        pass

    @abstractmethod
    def delete(self, db: Session, message_id: UUID, token: str) -> None:
        pass
