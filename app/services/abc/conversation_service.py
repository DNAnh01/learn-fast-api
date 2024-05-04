import uuid
from abc import ABC, abstractmethod
from typing import List, Optional
from sqlalchemy.orm import Session

from app.schemas.conversation import ConversationCreate, ConversationOut
from app.schemas.user_subscription_plan import UserSubscriptionPlan


class ConversationService(ABC):

    @abstractmethod
<<<<<<< HEAD
    def create(self, db: Session, conversation_create: ConversationCreate, chatbot_id: uuid.UUID,  current_user_membership: UserSubscriptionPlan) -> ConversationOut:
        pass

    @abstractmethod
    def get_one_with_filter_or_none(self, db: Session, current_user_membership: UserSubscriptionPlan, filter: dict) -> Optional[ConversationOut]:
        pass

    @abstractmethod
    def check_conversation(self, db: Session, current_user_membership: UserSubscriptionPlan, conversation_id: str, chatbot_id: str, client_ip: str) -> ConversationOut:
        pass

=======
    def create(self, db: Session, chatbot_id: str, client_ip: str) -> ConversationOut:
        pass

    @abstractmethod
    def get_one_with_filter_or_none(self, db: Session, filter: dict) -> Optional[ConversationOut]:
        pass

    @abstractmethod
    def get_all_or_none(self, db: Session, current_user_membership: UserSubscriptionPlan) -> Optional[List[ConversationOut]]:
        pass

    @abstractmethod
    def check_conversation(self, db: Session, conversation_id: str, chatbot_id: str, client_ip: str) -> ConversationOut:
        pass

    @abstractmethod
    def get_all_or_none(self, db: Session, current_user_membership: UserSubscriptionPlan) -> Optional[
        List[ConversationOut]]:
        pass

    @abstractmethod
    def load_messsages(self, conversation_id: str, db: Session, current_user_membership: UserSubscriptionPlan):
        pass

    @abstractmethod
    def join_conversation(self, conversation_id: str, db: Session, current_user_membership: UserSubscriptionPlan):
        pass

    @abstractmethod
    def message(self, conversation_id: str, message: str, db: Session, current_user_membership: UserSubscriptionPlan):
        pass
>>>>>>> origin/feature/MessageAndConversation
