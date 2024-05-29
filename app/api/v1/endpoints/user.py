import uuid

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.api import deps
from app.core import oauth2

from app.schemas.user_subscription_plan import UserSubscriptionPlan

from app.services.abc.user_service import UserService
from app.services.impl.user_service_impl import UserServiceImpl
from app.schemas.user import (
    UserCreate,
    UserInDB,
    UserOut,
    UserSignInWithGoogle,
    UserUpdate,
    UpdatePassword,
)


router = APIRouter()

user_service = UserServiceImpl()


@router.get("/profile", response_model=UserOut, status_code=status.HTTP_200_OK)
def get_profile(
    current_user_membership: UserSubscriptionPlan = Depends(
        oauth2.get_current_user_membership_info_by_token
    ),
    db: Session = Depends(deps.get_db),
):
    user = user_service.get_profile(
        db=db, current_user_membership=current_user_membership
    )
    return user


@router.put(
    "/edit/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model=UserOut,
)
def update(
    user_id: str,
    user_update: UserUpdate,
    current_user_membership: UserSubscriptionPlan = Depends(
        oauth2.get_current_user_membership_info_by_token
    ),
    db: Session = Depends(deps.get_db),
) -> UserOut:
    updated_user = user_service.update_one_with_filter(
        db=db,
        user_update=user_update,
        current_user_membership=current_user_membership,
        filter={"id": user_id},
    )
    return updated_user


@router.post("/{user_id}/change-password")
async def change_password(
    change_password: UpdatePassword,
    user_id: str,
    current_user_membership: UserSubscriptionPlan = Depends(
        oauth2.get_current_user_membership_info_by_token
    ),
    db: Session = Depends(deps.get_db),
):
    return await user_service.change_password(
        db=db, current_user_membership=current_user_membership, user_id=user_id, password=change_password
    )
