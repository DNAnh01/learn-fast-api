from typing import Optional

from sqlalchemy.orm import Session

from app.common.logger import setup_logger
from app.crud.crud_subscription_plan import crud_subscription_plan
from app.schemas.subscription_plan import (SubscriptionPlanCreate,
                                           SubscriptionPlanOut,
                                           SubscriptionPlanUpdate)
from app.services.abc.subscription_plan_service import SubscriptionPlanService

logger = setup_logger()


class SubscriptionPlanServiceImpl(SubscriptionPlanService):

    def __init__(self):
        self.__crud_subscription_plan = crud_subscription_plan

    def create(
        self, db: Session, subscription_plan: SubscriptionPlanCreate
    ) -> SubscriptionPlanOut:
        subscription_plan_found = self.get_one_with_filter_or_none(
            db=db, filter={"plan_title": subscription_plan.plan_title}
        )
        if subscription_plan_found is not None:
            return subscription_plan_found
        try:
            subscription_plan_created = self.__crud_subscription_plan.create(
                db=db, obj_in=subscription_plan
            )
        except Exception as subscription_plan_exec:
            logger.error(
                f"Error in {__name__}.{self.__class__.__name__}.create: {subscription_plan_exec}"
            )
            raise subscription_plan_exec
        if subscription_plan_created:
            result: SubscriptionPlanOut = SubscriptionPlanOut(
                **subscription_plan_created.__dict__
            )
        return result

    def get_one_with_filter_or_fail(
        self, db: Session, filter: dict
    ) -> SubscriptionPlanOut:
        try:
            subscription_plan_found = self.__crud_subscription_plan.get_one_by_or_fail(
                db=db, filter=filter
            )
        except Exception as subscription_plan_exec:
            logger.error(
                f"Error in {__name__}.{self.__class__.__name__}.get_one_with_filter: {subscription_plan_exec}"
            )
            raise subscription_plan_exec
        if subscription_plan_found:
            result: SubscriptionPlanOut = SubscriptionPlanOut(
                **subscription_plan_found.__dict__
            )
        return result

    def get_one_with_filter_or_none(
        self, db: Session, filter: dict
    ) -> Optional[SubscriptionPlanOut]:
        subscription_plan_found = self.__crud_subscription_plan.get_one_by(
            db=db, filter=filter
        )
        if subscription_plan_found:
            result: SubscriptionPlanOut = SubscriptionPlanOut(
                **subscription_plan_found.__dict__
            )
            return result
        return None

    def update_one_with_filter(
        self, db: Session, filter: dict, subscription_plan: SubscriptionPlanUpdate
    ) -> SubscriptionPlanOut:
        try:
            subscription_plan_updated = self.__crud_subscription_plan.update_one_by(
                db=db, filter=filter, obj_in=subscription_plan
            )
        except Exception as subscription_plan_exec:
            logger.error(
                f"Error in {__name__}.{self.__class__.__name__}.update_one_with_filter: {subscription_plan_exec}"
            )
            raise subscription_plan_exec
        if subscription_plan_updated:
            result: SubscriptionPlanOut = SubscriptionPlanOut(
                **subscription_plan_updated.__dict__
            )
        return result

    def get_all(self, db: Session) -> list[SubscriptionPlanOut]:
        try:
            subscription_plans = self.__crud_subscription_plan.get_multi_not_paging(
                db=db
            )
        except Exception as subscription_plan_exec:
            logger.error(
                f"Error in {__name__}.{self.__class__.__name__}.get_all: {subscription_plan_exec}"
            )
            raise subscription_plan_exec

        if subscription_plans:
            results = [
                SubscriptionPlanOut(**subscription_plan.__dict__)
                for subscription_plan in subscription_plans
            ]
        return results
