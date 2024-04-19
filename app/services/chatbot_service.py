from abc import ABC, abstractmethod
from typing import List, Optional

from sqlalchemy.orm import Session

from app.schemas.chatbot import ChatBotCreate, ChatBotOut, ChatBotUpdate
from app.schemas.user_subscription_plan import UserSubscriptionPlan


class ChatBotService(ABC):

    @abstractmethod
    def create(self, db: Session, chatbot_create: ChatBotCreate, current_user_membership: UserSubscriptionPlan) -> ChatBotOut:
        pass

    @abstractmethod
    def get_all_or_none(self, db: Session, current_user_membership: UserSubscriptionPlan) -> Optional[List[ChatBotOut]]:
        pass


    @abstractmethod
    def get_one_with_filter_or_none(self, db: Session, current_user_membership: UserSubscriptionPlan, filter: dict) -> Optional[ChatBotOut]:
        pass

    @abstractmethod
    def update_one_with_filter(
        self, db: Session, chatbot_update: ChatBotUpdate, current_user_membership: UserSubscriptionPlan, filter: dict) -> ChatBotOut:
        pass
