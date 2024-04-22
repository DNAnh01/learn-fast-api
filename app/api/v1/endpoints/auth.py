from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from starlette.requests import Request

from app.api import deps
from app.core import oauth2
from app.core.google_auth import oauth
from app.schemas.auth import ChangePassword, Email
from app.schemas.token import Token
from app.schemas.user import UserOut, UserSignIn, UserSignUp
from app.services.abc.auth_service import AuthService
from app.services.impl.auth_service_impl import AuthServiceImpl

router = APIRouter()
auth_service: AuthService = AuthServiceImpl()


@router.post("/sign-up", status_code=status.HTTP_201_CREATED, response_model=UserOut)
async def sign_up(
    user: UserSignUp,
    db: Session = Depends(deps.get_db)
) -> UserOut:
    return await auth_service.sign_up(db=db, user=user)


@router.post("/sign-in", status_code=status.HTTP_200_OK, response_model=Token)
def sign_in(
    user: UserSignIn,
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
    db: Session = Depends(deps.get_db),
):
    return await auth_service.handle_google_callback(request, db)


@router.get("/verification")
def verification(
    token: str,
    db: Session = Depends(deps.get_db),
):
    return auth_service.verify_user(db=db, token=token)


@router.get("/sign-out", status_code=status.HTTP_200_OK)
def sign_out(
    get_current_user: UserOut = Depends(oauth2.get_current_user),
    db: Session = Depends(deps.get_db),
):
    return auth_service.sign_out(db=db, get_current_user=get_current_user)


@router.post("/forgot-password")
async def forgot_password(
    email: Email,
    db: Session = Depends(deps.get_db),
):
    return await auth_service.forgot_password(db=db, email=email)


@router.get("/change-password")
async def change_password(
    password: ChangePassword,
    get_current_user: UserOut = Depends(oauth2.get_current_user),
    db: Session = Depends(deps.get_db),
):
    return await auth_service.change_password(db=db, get_current_user=get_current_user, password=password)