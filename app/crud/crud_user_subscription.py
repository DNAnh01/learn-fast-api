from app.crud.base import CRUDBase
from app.models.user_subscription import UserSubscription
from app.schemas.user_subscription import UserSubscriptionCreate, UserSubscriptionUpdate


class CRUDUserSubscription(
    CRUDBase[UserSubscription, UserSubscriptionCreate, UserSubscriptionUpdate]
):
    pass


crud_user_subscription = CRUDUserSubscription(UserSubscription)
