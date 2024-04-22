from abc import ABC, abstractmethod
from typing import Optional

from sqlalchemy.orm import Session

from app.schemas.subscription_plan import (
    SubscriptionPlanCreate,
    SubscriptionPlanOut,
    SubscriptionPlanUpdate,
)


class SubscriptionPlanService(ABC):

    @abstractmethod
    def create(
        self, db: Session, subscription_plan: SubscriptionPlanCreate
    ) -> SubscriptionPlanOut:
        pass

    @abstractmethod
    def get_one_with_filter_or_fail(
        self, db: Session, filter: dict
    ) -> SubscriptionPlanOut:
        pass

    @abstractmethod
    def get_one_with_filter_or_none(
        self, db: Session, filter: dict
    ) -> Optional[SubscriptionPlanOut]:
        pass

    @abstractmethod
    def update_one_with_filter(
        self, db: Session, filter: dict, subscription_plan: SubscriptionPlanUpdate
    ) -> SubscriptionPlanOut:
        pass

    @abstractmethod
    def get_all(self, db: Session) -> list[SubscriptionPlanOut]:
        pass
