import uuid
from abc import ABC, abstractmethod

from sqlalchemy.orm import Session

from app.schemas.conversation import ConversationCreate, ConversationOut
from app.schemas.user_subscription_plan import UserSubscriptionPlan


class ConversationService(ABC):

    @abstractmethod
    def create(self, db: Session, conversation_create: ConversationCreate, chatbot_id: uuid.UUID,  current_user_membership: UserSubscriptionPlan) -> ConversationOut:
        pass

