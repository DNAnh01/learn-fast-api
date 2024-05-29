from abc import ABC, abstractmethod
from typing import Optional

from sqlalchemy.orm import Session

from app.schemas.user_subscription import (
    UserSubscriptionCreate,
    UserSubscriptionOut,
    UserSubscriptionUpdate,
)


class UserSubscriptionService(ABC):

    @abstractmethod
    def create(
        self, db: Session, user_subscription: UserSubscriptionCreate
    ) -> UserSubscriptionOut:
        pass

    @abstractmethod
    def get_one_with_filter_or_fail(
        self, db: Session, filter: dict
    ) -> UserSubscriptionOut:
        pass

    @abstractmethod
    def get_one_with_filter_or_none(
        self, db: Session, filter: dict
    ) -> Optional[UserSubscriptionOut]:
        pass

    @abstractmethod
    def update_one_with_filter(
        self, db: Session, filter: dict, user_subscription: UserSubscriptionUpdate
    ) -> UserSubscriptionOut:
        pass
