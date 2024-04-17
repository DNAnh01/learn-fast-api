# from fastapi import APIRouter, Depends, status
# from sqlalchemy.orm import Session

# from app.api import deps
# from app.core.oauth2 import get_current_admin_user, get_current_user
# from app.schemas.subscription_plan import (SubscriptionPlanCreate,
#                                            SubscriptionPlanOut,
#                                            SubscriptionPlanUpdate)
# from app.schemas.user import UserOut
# from app.services.subscription_plan_service_impl import \
#     SubscriptionPlanServiceImpl

# router = APIRouter()

# @router.post("/", status_code=status.HTTP_201_CREATED, response_model=SubscriptionPlanOut)
# async def create(
#     subscription_plan: SubscriptionPlanCreate,
#     current_user: UserOut = Depends(get_current_admin_user),
#     subscription_plan_service: SubscriptionPlanServiceImpl = Depends(),
#     db: Session = Depends(deps.get_db)
# ):
#     return await subscription_plan_service.create(db=db, subscription_plan=subscription_plan)

# @router.get("/", status_code=status.HTTP_200_OK, response_model=list[SubscriptionPlanOut])
# async def get_all(
#     current_user: UserOut = Depends(get_current_user),
#     subscription_plan_service: SubscriptionPlanServiceImpl = Depends(),
#     db: Session = Depends(deps.get_db)
# ):
#     return await subscription_plan_service.get_all(db=db)
