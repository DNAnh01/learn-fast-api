import uuid
from datetime import datetime, timedelta

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.common.logger import setup_logger
from app.crud.crud_user_subscription_plan import crud_user_subscription_plan
from app.schemas.user import UserOut
from app.schemas.user_subscription import UserSubscriptionCreate
from app.schemas.user_subscription_plan import UserSubscriptionPlan
from app.services.membership_service import MembershipService
from app.services.subscription_plan_service_impl import \
    SubscriptionPlanServiceImpl
from app.services.user_subscription_service_impl import \
    UserSubscriptionServiceImpl

logger = setup_logger()


class MembershipServiceImpl(MembershipService):
    def __init__(self):
        self.__subscription_plan_service = SubscriptionPlanServiceImpl()
        self.__user_subscription_service = UserSubscriptionServiceImpl()
        self.__crud_user_subscription_plan = crud_user_subscription_plan

    def create_default_subscription(self, db: Session, new_user: UserOut):
        default_plan = self.__subscription_plan_service.get_one_with_filter_or_none(
            db=db, filter={"plan_title": "monthly_free"}
        )
        if default_plan is None:
            logger.exception(
                f"Exception in {__name__}.{self.__class__.__name__}.create_default_subscription: Default plan not found"
            )
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Default plan not found"
            )
        self.__user_subscription_service.create(
            db=db,
            user_subscription=UserSubscriptionCreate(
                user_id=new_user.id,
                plan_id=default_plan.id,
                expire_at=datetime.now() + timedelta(days=30),
                is_active=True,
                created_at=datetime.now(),
                updated_at=datetime.now(),
                deleted_at=None,
            ),
        )

    def get_user_membership_by_user_id(self, db: Session, user_id: uuid.UUID) -> UserSubscriptionPlan:
        return self.__crud_user_subscription_plan.get_user_membership_info(
            db=db,
            user_id=user_id
        )