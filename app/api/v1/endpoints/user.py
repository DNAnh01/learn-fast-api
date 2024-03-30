from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api import deps
from app.common.parameters import common_filter_parameters
from app.schemas.user import User, UserCreate, Users
from app.services.user_service_impl import UserServiceImpl

router = APIRouter()
user_service = UserServiceImpl()


@router.get("/", response_model=Users)
def read_users(
    db: Session = Depends(deps.get_db),
    filter_param: str = Depends(common_filter_parameters),
) -> Any:

    return user_service.get_multi(db, filter_param=filter_param)


@router.post("/", response_model=User)
def create_user(
    *,
    db: Session = Depends(deps.get_db),
    user_in: UserCreate,
) -> Any:
    user = user_service.create(db=db, user=user_in)
    return user
