from abc import ABC, abstractmethod
from typing import List, Optional

from sqlalchemy.orm import Session

from app.schemas.chatbot import ChatBotCreate, ChatBotOut, ChatBotUpdate
from app.schemas.user_subscription_plan import UserSubscriptionPlan
from app.schemas.conversation import ConversationCreate,ConversationUpdate,ConversationOut
from app.schemas.message import MessageCreate,MessageUpdate,MessageOut


class ChatBotService(ABC):

    @abstractmethod
    def create(self, db: Session, chatbot_create: ChatBotCreate, current_user_membership: UserSubscriptionPlan) -> ChatBotOut:
        pass

    @abstractmethod
    def get_all_or_none(self, db: Session, current_user_membership: UserSubscriptionPlan) -> Optional[List[ChatBotOut]]:
        pass


    @abstractmethod
<<<<<<< HEAD
    def get_one_with_filter_or_none(self, db: Session, current_user_membership: UserSubscriptionPlan, filter: dict) -> Optional[ChatBotOut]:
=======
    def get_one_with_filter_or_none(self, db: Session, filter: dict) -> Optional[ChatBotOut]:
>>>>>>> origin/feature/MessageAndConversation
        pass

    @abstractmethod
    def update_one_with_filter(
        self, db: Session, chatbot_update: ChatBotUpdate, current_user_membership: UserSubscriptionPlan, filter: dict) -> ChatBotOut:
        pass

    @abstractmethod
    def message(
<<<<<<< HEAD
            self, db: Session, chatbot_id: str, conversation_id: str, message: str, current_user_membership: UserSubscriptionPlan, client_ip: str) -> MessageOut:
=======
            self, db: Session, chatbot_id: str, conversation_id: str, message: str, client_ip: str) -> MessageOut:
>>>>>>> origin/feature/MessageAndConversation
        pass

    @abstractmethod
    def handle_message(
<<<<<<< HEAD
            self, db: Session, chatbot_id: str, conversation_id: str, message: str, current_user_membership: UserSubscriptionPlan) -> MessageOut:
=======
            self, db: Session, chatbot_id: str, conversation_id: str, message: str) -> MessageOut:
>>>>>>> origin/feature/MessageAndConversation
        pass

