import uuid
from abc import ABC, abstractmethod

from sqlalchemy.orm import Session

from app.schemas.user import UserOut
from app.schemas.user_subscription_plan import UserSubscriptionPlan


class MembershipService(ABC):
    @abstractmethod
    def create_default_subscription(self, db: Session, new_user: UserOut):
        pass

    @abstractmethod
    def get_user_membership_by_user_id(
        self, db: Session, user_id: uuid.UUID
    ) -> UserSubscriptionPlan:
        pass
