from abc import ABC, abstractmethod
from typing import List, Optional

from sqlalchemy.orm import Session

from app.schemas.chatbot import (
    ChatBotCreate,
    ChatBotOut,
    ChatBotUpdate,
    ChatBotInDB,
)
from app.schemas.user_subscription_plan import UserSubscriptionPlan
from app.schemas.conversation import (
    ConversationCreate,
    ConversationUpdate,
    ConversationOut,
)
from app.schemas.message import MessageCreate, MessageUpdate, MessageOut


class ChatBotService(ABC):

    @abstractmethod
    def create(
        self,
        db: Session,
        user_id: str,
        chatbot_create: ChatBotCreate,
        current_user_membership: UserSubscriptionPlan,
    ) -> ChatBotOut:
        pass

    @abstractmethod
    def get_all_or_none(
        self, db: Session, user_id: str
    ) -> Optional[List[ChatBotOut]]:
        pass

    @abstractmethod
    def get_one_with_filter_or_none(
        self, db: Session, filter: dict
    ) -> Optional[ChatBotOut]:
        pass

    @abstractmethod
    def update_one_with_filter(
        self,
        db: Session,
        chatbot_update: ChatBotUpdate,
        current_user_membership: UserSubscriptionPlan,
        filter: dict,
    ) -> ChatBotOut:
        pass

    @abstractmethod
    def message(
        self,
        db: Session,
        chatbot_id: str,
        conversation_id: str,
        message: str,
        client_ip: str,
    ) -> MessageOut:
        pass

    @abstractmethod
    def message_with_auth(
        self,
        db: Session,
        chatbot_id: str,
        conversation_id: str,
        message: str,
        client_ip: str,
        current_user_membership: UserSubscriptionPlan,
    ) -> MessageOut:
        pass

    @abstractmethod
    def handle_message(
        self, db: Session, chatbot_id: str, conversation_id: str, message: str
    ) -> MessageOut:
        pass

    @abstractmethod
    def delete(
        self,
        db: Session,
        user_id: str,
        chatbot_id: str,
        current_user_membership: UserSubscriptionPlan,
    ):
        pass
