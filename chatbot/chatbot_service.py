from abc import ABC, abstractmethod

from sqlalchemy.orm import Session

from app.schemas.chatbot import ChatBotCreate, ChatBotUpdate, ChatBotOut


class ChatBotService(ABC):

    @abstractmethod
    def create(self, db: Session, brain: ChatBotCreate, token: str) -> ChatBotOut:
        pass

    @abstractmethod
    def update(self, db: Session, brain: ChatBotUpdate) -> ChatBotOut:
        pass
