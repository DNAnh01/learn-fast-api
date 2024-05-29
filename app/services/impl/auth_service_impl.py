import asyncio
import uuid
from datetime import datetime
from typing import Union
from urllib.parse import urlencode

from fastapi import Depends, HTTPException, Response, status
from fastapi.responses import JSONResponse, RedirectResponse
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound
from starlette.requests import Request

from app.common import generate, send_email, utils
from app.common.generate import generate_random_string
from app.common.logger import setup_logger
from app.core import google_auth, oauth2
from app.core.config import settings
from app.crud.crud_user import crud_user
from app.crud.crud_user_session import crud_user_session
from app.schemas.auth import ChangePassword, Email
from app.schemas.token import Token
from app.schemas.user import (
    UserCreate,
    UserInDB,
    UserOut,
    UserSignIn,
    UserSignInWithGoogle,
    UserSignUp,
    UserUpdate,
)
from app.schemas.auth import (
    EmailSchema,
)
from app.schemas.user_session import UserSessionCreate, UserSessionUpdate
from app.services.abc.auth_service import AuthService
from app.services.abc.email_service import EmailService
from app.services.impl.email_service_impl import EmailServiceImpl
from app.services.abc.membership_service import MembershipService
from app.services.impl.membership_service_impl import MembershipServiceImpl
from app.services.abc.user_service import UserService
from app.services.impl.user_service_impl import UserServiceImpl
from app.services.abc.user_session_service import UserSessionService
from app.services.impl.user_session_service_impl import UserSessionServiceImpl

logger = setup_logger()


class AuthServiceImpl(AuthService):

    def __init__(self) -> None:
        self.__crud_user = crud_user
        self.__user_service: UserService = UserServiceImpl()
        self.__user_session_service: UserSessionService = (
            UserSessionServiceImpl()
        )
        self.__email_service: EmailService = EmailServiceImpl()
        self.__membership_service: MembershipService = MembershipServiceImpl()

    async def sign_up(self, db: Session, user: UserSignUp):
        hashed_password = utils.hash(user.password)

        # Check original email
        is_sended = await self.__email_service.send_verification_email(
            user_info={"email": user.email, "name": user.email},
            redirect_url=f"{settings.REDIRECT_FRONTEND_URL}/",
        )
        # logger.warning(f"Email sended: {is_sended}")
        if is_sended:
            try:
                new_user = self.__user_service.create(
                    db=db,
                    user=UserCreate(
                        email=user.email,
                        password_hash=hashed_password,
                        is_active=True,
                        created_at=datetime.now(),
                        updated_at=datetime.now(),
                        deleted_at=None,
                    ),
                )
            except Exception as e:
                if "User already exists" in str(e):
                    raise HTTPException(
                        status_code=status.HTTP_409_CONFLICT,
                        detail="User already exists",
                    )
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email not sended",
            )

        self.__membership_service.create_default_subscription(db, new_user)

        return new_user

    def sign_in(self, db: Session, user_credentials: UserSignIn) -> Token:
        user_found: UserInDB = (
            self.__user_service.get_one_with_filter_or_none_db(
                db=db, filter={"email": user_credentials.email}
            )
        )
        if user_found is None:
            logger.exception(
                f"Exception in {__name__}.{self.__class__.__name__}.sign_in: User not found: {user_credentials.email}"
            )
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail=f"User not found"
            )

        if not utils.verify(
            user_credentials.password, user_found.password_hash
        ):
            logger.exception(
                f"Exception in {__name__}.{self.__class__.__name__}.sign_in: Invalid password: {user_credentials.email}"
            )
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Invalid Credentials",
            )
        access_token: str = oauth2.create_access_token(
            data={"user_id": str(user_found.id)}
        )
        user_session_created = self.__user_session_service.create(
            db=db,
            session=UserSessionCreate(
                token=access_token,
                user_id=user_found.id,
                is_active=True,
                created_at=datetime.now(),
                updated_at=datetime.now(),
                deleted_at=None,
                expires_at=utils.get_expires_at(),
            ),
        )
        return Token(
            access_token=user_session_created.token, token_type="bearer"
        )

    def verify_user(self, db: Session, token: str) -> Token:
        current_user = oauth2.get_current_user(db=db, token=token)

        self.__user_service.update_is_verified(
            db=db,
            email=current_user.email,
        )
        user_session_updated = (
            self.__user_session_service.update_one_with_filter(
                db=db,
                filter={"token": token},
                session=UserSessionUpdate(
                    token=token,
                    expires_at=utils.get_expires_at(),
                    updated_at=datetime.now(),
                ),
            )
        )
        return RedirectResponse(
            url=f"{settings.REDIRECT_FRONTEND_URL}/home?token={user_session_updated.token}"
        )

    def create_session(self, db: Session, user_id: uuid.UUID):
        access_token = oauth2.create_access_token(
            data={"user_id": str(user_id)}
        )
        user_session_created = self.__user_session_service.create(
            db=db,
            session=UserSessionCreate(
                token=access_token,
                user_id=user_id,
                is_active=True,
                created_at=datetime.now(),
                updated_at=datetime.now(),
                deleted_at=None,
                expires_at=utils.get_expires_at(),
            ),
        )
        return user_session_created

    async def handle_google_callback(self, request: Request, db: Session):
        token = None
        while not token:
            try:
                token = await google_auth.authorize_access_token(request)
            except Exception as e:
                logger.exception(
                    f"Exception in {__name__}.{self.__class__.__name__}.handle_google_callback: {e}"
                )
                await asyncio.sleep(1)  # wait for 1 second before trying again

        try:
            user_info = token.get("userinfo")
            logger.info(f"User info: {user_info}")
        except Exception as e:
            logger.exception(
                f"Exception in {__name__}.{self.__class__.__name__}.handle_google_callback: {e}"
            )
            return JSONResponse(
                status_code=400, content={"message": "Error getting user info"}
            )
        if user_info:
            request.session["user"] = dict(user_info)
            user_found = self.__user_service.get_one_with_filter_or_none(
                db=db, filter={"email": user_info["email"]}
            )
            if user_found is not None:
                session_created = self.create_session(db, user_found.id)
                if not user_found.is_verified:
                    is_sended = await self.__email_service.send_verification_email(
                        user_info=user_info,
                        redirect_url=f"{settings.REDIRECT_BACKEND_URL}/api/v1/auth/verification?token={session_created.token}",
                    )
                    if is_sended:
                        return RedirectResponse(
                            url=f"{settings.REDIRECT_FRONTEND_URL}/success"
                        )
                    return RedirectResponse(
                        url=f"{settings.REDIRECT_FRONTEND_URL}/error"
                    )

                return RedirectResponse(
                    url=f"{settings.REDIRECT_FRONTEND_URL}/home?token={session_created.token}"
                )

            else:
                user_created_with_google = UserSignInWithGoogle(
                    email=user_info["email"],
                    display_name=user_info["name"],
                    password_hash=user_info["at_hash"],
                    avatar_url=user_info["picture"],
                    is_verified=False,
                    is_active=True,
                    created_at=datetime.now(),
                    updated_at=datetime.now(),
                    deleted_at=None,
                    user_role="user",
                )

                new_user = self.__user_service.create_user_with_google(
                    db=db, user=user_created_with_google
                )

                self.__membership_service.create_default_subscription(
                    db, new_user
                )

                session_created = self.create_session(db, new_user.id)

                is_sended = await self.__email_service.send_verification_email(
                    user_info=user_info,
                    redirect_url=f"{settings.REDIRECT_BACKEND_URL}/api/v1/auth/verification?token={session_created.token}",
                )
                if is_sended:
                    return RedirectResponse(
                        url=f"{settings.REDIRECT_FRONTEND_URL}/success"
                    )
                return RedirectResponse(
                    url=f"{settings.REDIRECT_FRONTEND_URL}/error"
                )

    def sign_out(self, db: Session, get_current_user: UserOut):
        try:
            self.__user_session_service.remove_one_with_filter(
                db=db, filter={"user_id": get_current_user.id}
            )
            return JSONResponse(
                status_code=200, content={"message": "Sign out successful"}
            )
        except NoResultFound:
            logger.exception(
                f"Exception in {__name__}.{self.__class__.__name__}.sign_out: User not found: {get_current_user.id}"
            ),
            raise HTTPException(detail="Sign out failed", status_code=400)

    async def forgot_password(self, db: Session, email: EmailSchema):
        user_found = self.__crud_user.get_one_by(
            db=db, filter={"email": email.email}
        )

        if user_found is None:
            logger.error(
                f"Error in {__name__}.{self.__class__.__name__}.forgot_password: User not found"
            )
            return JSONResponse(
                status_code=404,
                content={"status": 404, "message": "User not found"},
            )
        password_reset = generate.generate_random_string(8)
        user_updated = self.__crud_user.update_one_by(
            db=db,
            filter={"id": user_found.id},
            obj_in={"password_hash": utils.hash(password_reset)},
        )
        if user_updated is None:
            logger.error(
                f"Error in {__name__}.{self.__class__.__name__}.forgot_password: Password reset failed"
            )
            return JSONResponse(
                status_code=500,
                content={"status": 500, "message": "Update password failed"},
            )
        is_sended = await send_email.send_reset_password_email(
            email=user_found.email,
            display_name=user_found.display_name,
            password_reset=password_reset,
        )
        if is_sended:
            return JSONResponse(
                status_code=200,
                content={"status": 200, "message": "Reset password successful"},
            )
        return JSONResponse(
            status_code=500,
            content={"status": 500, "message": "Reset password failed"},
        )

    async def change_password(
        self, db: Session, get_current_user: UserOut, password: ChangePassword
    ):
        user_found = self.__user_service.get_one_with_filter_or_none(
            db=db, filter={"id": get_current_user.id}
        )
        if user_found is None:
            logger.exception(
                f"Exception in {__name__}.{self.__class__.__name__}.reset_password: User not found"
            )
            raise HTTPException(status_code=400, detail="User not found")

        try:
            self.__user_service.update_one_with_filter(
                db=db,
                filter={
                    "password_hash": utils.hash(password.password_old),
                    "id": get_current_user.id,
                },
                user=UserUpdate(
                    password_hash=utils.hash(password.password_new)
                ),
            )
        except Exception as e:
            logger.exception(
                f"Exception in {__name__}.{self.__class__.__name__}.change_password: {e}"
            )
            raise HTTPException(status_code=400, detail="Password not changed")
        return JSONResponse(
            status_code=200,
            content={"message": "Password changed successfully"},
        )
