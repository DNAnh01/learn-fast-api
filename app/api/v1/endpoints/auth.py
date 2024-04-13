from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from starlette.requests import Request

from app.api import deps
from app.core.google_auth import oauth
from app.models.session import Session
from app.schemas.token import Token
from app.schemas.user import UserOut, UserSignIn, UserSignUp
from app.services.auth_service_impl import AuthServiceImpl

router = APIRouter()


@router.post("/sign-up", status_code=status.HTTP_201_CREATED, response_model=UserOut)
def sign_up(
    user: UserSignUp,
    auth_service: AuthServiceImpl = Depends(),
    db: Session = Depends(deps.get_db),
) -> UserOut:
    return auth_service.sign_up(db=db, user=user)


@router.post("/sign-in", status_code=status.HTTP_200_OK, response_model=Token)
def sign_in(
    user: UserSignIn,
    auth_service: AuthServiceImpl = Depends(),
    db: Session = Depends(deps.get_db),
) -> Token:
    return auth_service.sign_in(db=db, user_credentials=user)


@router.get("/sign-in-with-google")
async def sign_in_with_google(request: Request):
    redirect_uri = request.url_for("callback")
    return await oauth.google.authorize_redirect(request, redirect_uri)


@router.get("/callback")
async def callback(
    request: Request,
    auth_service: AuthServiceImpl = Depends(),
    db: Session = Depends(deps.get_db),
):
    return await auth_service.handle_google_callback(request, db)


@router.get("/verification")
async def verification(
    token: str,
    auth_service: AuthServiceImpl = Depends(),
    db: Session = Depends(deps.get_db),
):
    return await auth_service.verify_user(db=db, token=token)


@router.post("/sign-out", status_code=status.HTTP_200_OK)
def sign_out(
    token: str,
    auth_service: AuthServiceImpl = Depends(),
    db: Session = Depends(deps.get_db),
):
    return auth_service.sign_out(db=db, token=token)


@router.post("/forgot-password")
async def forgot_password(
    email: str,
    auth_service: AuthServiceImpl = Depends(),
    db: Session = Depends(deps.get_db),
):
    return await auth_service.forgot_password(db=db, email=email)


@router.get("/reset-password")
async def reset_password(
    token: str,
    auth_service: AuthServiceImpl = Depends(),
    db: Session = Depends(deps.get_db),
):
    return await auth_service.reset_password(db=db, token=token)
