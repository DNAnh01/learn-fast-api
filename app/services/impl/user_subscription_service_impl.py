from typing import Optional

from sqlalchemy.orm import Session

from app.common.logger import setup_logger
from app.crud.crud_user_subscription import crud_user_subscription
from app.schemas.user_subscription import (
    UserSubscriptionCreate,
    UserSubscriptionOut,
    UserSubscriptionUpdate,
)
from app.services.abc.user_subscription_service import UserSubscriptionService

logger = setup_logger()


class UserSubscriptionServiceImpl(UserSubscriptionService):

    def __init__(self):
        self.__crud_user_subscription = crud_user_subscription

    def create(
        self, db: Session, user_subscription: UserSubscriptionCreate
    ) -> UserSubscriptionOut:
        user_subscription_found = self.get_one_with_filter_or_none(
            db=db, filter={"user_id": user_subscription.user_id}
        )
        if user_subscription_found is not None:
            return user_subscription_found
        try:
            user_subscription_created = self.__crud_user_subscription.create(
                db=db, obj_in=user_subscription
            )
        except Exception as user_subscription_exec:
            logger.error(
                f"Error in {__name__}.{self.__class__.__name__}.create: {user_subscription_exec}"
            )
            raise user_subscription_exec
        if user_subscription_created:
            result: UserSubscriptionOut = UserSubscriptionOut(
                **user_subscription_created.__dict__
            )
        return result

    def get_one_with_filter_or_fail(
        self, db: Session, filter: dict
    ) -> UserSubscriptionOut:
        try:
            user_subscription_found = self.__crud_user_subscription.get_one_by_or_fail(
                db=db, filter=filter
            )
        except Exception as user_subscription_exec:
            logger.error(
                f"Error in {__name__}.{self.__class__.__name__}.get_one_with_filter: {user_subscription_exec}"
            )
            raise user_subscription_exec
        if user_subscription_found:
            result: UserSubscriptionOut = UserSubscriptionOut(
                **user_subscription_found.__dict__
            )
        return result

    def get_one_with_filter_or_none(
        self, db: Session, filter: dict
    ) -> Optional[UserSubscriptionOut]:
        user_found = self.__crud_user_subscription.get_one_by(db=db, filter=filter)
        if user_found:
            result: UserSubscriptionOut = UserSubscriptionOut(**user_found.__dict__)
            return result
        return None

    def update_one_with_filter(
        self, db: Session, filter: dict, user_subscription: UserSubscriptionUpdate
    ) -> UserSubscriptionOut:
        try:
            user_subscription_updated = self.__crud_user_subscription.update_one_by(
                db=db, filter=filter, obj_in=user_subscription
            )
        except Exception as user_subscription_exec:
            logger.error(
                f"Error in {__name__}.{self.__class__.__name__}.update_one_with_filter: {user_subscription_exec}"
            )
            raise user_subscription_exec
        if user_subscription_updated:
            result: UserSubscriptionOut = UserSubscriptionOut(
                **user_subscription_updated.__dict__
            )
        return result
