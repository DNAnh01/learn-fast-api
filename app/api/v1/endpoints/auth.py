from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.api import deps
from app.common import utils
from app.core import oauth2
from app.schemas.token import Token
from app.services.user_service import UserService
from app.services.user_service_impl import UserServiceImpl

router = APIRouter()
user_service: UserService = UserServiceImpl()


@router.post("/login", response_model=Token)
def login(
    user_credentials: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(deps.get_db),
):
    user = user_service.get_by_email(db=db, email=user_credentials.username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials"
        )

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials"
        )

    access_token = oauth2.create_access_token(data={"user_id": str(user.id)})

    return {"access_token": access_token, "token_type": "bearer"}
