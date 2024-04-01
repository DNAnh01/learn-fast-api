"""
    Sign up
    Sign in
    Sign in with Google
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api import deps
from app.common import utils
from app.core import oauth2
from app.schemas.token import Token
from app.schemas.user import UserCreate, UserLogin, UserOut
from app.services.auth_service_impl import AuthServiceImpl

router = APIRouter()

auth_service = AuthServiceImpl()

@router.post("/sign-up", status_code=status.HTTP_201_CREATED, response_model=UserOut)
def sign_up(user: UserCreate, db: Session = Depends(deps.get_db)) -> UserOut:
    new_user = auth_service.sign_up(db=db, user=user)
    return new_user

@router.post("/sign-in",status_code=status.HTTP_200_OK ,response_model=Token)
def sign_in(user: UserLogin, db: Session = Depends(deps.get_db)) -> Token:
    # TODO: Implement the sign-in logic

    token = auth_service.sign_in(db=db, user_credentials=user)
    return token


# TODO: Implement the sign-in with Google logic

