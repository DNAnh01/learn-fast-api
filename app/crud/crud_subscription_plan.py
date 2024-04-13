from app.crud.base import CRUDBase
from app.models.subscription_plan import SubscriptionPlan
from app.schemas.subscription_plan import SubscriptionPlanCreate, SubscriptionPlanUpdate


class CRUDSubscriptionPlan(
    CRUDBase[SubscriptionPlan, SubscriptionPlanCreate, SubscriptionPlanUpdate]
):
    pass


crud_subscription_plan = CRUDSubscriptionPlan(SubscriptionPlan)
