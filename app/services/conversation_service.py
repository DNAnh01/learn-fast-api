from abc import ABC, abstractmethod

from sqlalchemy.orm import Session
from app.schemas.token import Token

from app.models.conversation import Conversation
from app.schemas.conversation import ConversationCreate, ConversationUpdate, ConversationOut
from app.crud.crud_conversation import crud_conversation


class ConversationService(ABC):

    @abstractmethod
    def create(self, db: Session, conversation: ConversationCreate, token: str) -> ConversationOut:
        pass
