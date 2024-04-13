import asyncio
import uuid
from datetime import datetime, timedelta

from fastapi import HTTPException, Response, status
from fastapi.responses import JSONResponse, RedirectResponse
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound
from starlette.requests import Request

from app.common import utils
from app.common.generate import generate_random_string
from app.common.logger import setup_logger
from app.core import google_auth, oauth2
from app.schemas.session import SessionCreate, SessionUpdate
from app.schemas.token import Token
from app.schemas.user import (UserCreate, UserInDB, UserOut, UserSignIn,
                              UserSignInWithGoogle, UserSignUp, UserUpdate)
from app.schemas.user_subscription import UserSubscriptionCreate
from app.services.auth_service import AuthService
from app.services.email_service_impl import EmailServiceImpl
from app.services.session_service_impl import SessionServiceImpl
from app.services.subscription_plan_service_impl import \
    SubscriptionPlanServiceImpl
from app.services.user_service_impl import UserServiceImpl
from app.services.user_subscription_service_impl import \
    UserSubscriptionServiceImpl

logger = setup_logger()


class AuthServiceImpl(AuthService):

    def __init__(self) -> None:
        self.__user_service = UserServiceImpl()
        self.__session_service = SessionServiceImpl()
        self.__email_service = EmailServiceImpl()
        self.__user_subscription_service = UserSubscriptionServiceImpl()
        self.__subscription_plan_service = SubscriptionPlanServiceImpl()

    def sign_up(self, db: Session, user: UserSignUp) -> UserOut:
        hashed_password = utils.hash(user.password)
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

        default_plan = self.__subscription_plan_service.get_one_with_filter_or_none(
            db=db, filter={"plan_title": "monthly_free"}
        )
        if default_plan is None:
            logger.exception(
                f"Exception in {__name__}.{self.__class__.__name__}.sign_up: Default plan not found: monthly_free"
            )
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Default plan not found"
            )

        # logger.info(f"Default plan: {dict(default_plan)}")
        self.__user_subscription_service.create(
            db=db,
            user_subscription=UserSubscriptionCreate(
                user_id=new_user.id,
                plan_id=default_plan.id,
                expire_at=datetime.now() + timedelta(days=30),
                is_active=True,
                created_at=datetime.now(),
                updated_at=datetime.now(),
                deleted_at=None,
            ),
        )
        return new_user

    def sign_in(self, db: Session, user_credentials: UserSignIn) -> Token:
        user_found: UserInDB = self.__user_service.get_one_with_filter_or_none(
            db=db, filter={"email": user_credentials.email}
        )
        if user_found is None:
            logger.exception(
                f"Exception in {__name__}.{self.__class__.__name__}.sign_in: User not found: {user_credentials.email}"
            )
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials"
            )
        if not utils.verify(user_credentials.password, user_found.password_hash):
            logger.exception(
                f"Exception in {__name__}.{self.__class__.__name__}.sign_in: Invalid password: {user_credentials.email}"
            )
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials"
            )
        access_token: str = oauth2.create_access_token(
            data={"user_id": str(user_found.id)}
        )
        token_data = self.__session_service.create(
            db=db,
            session=SessionCreate(
                token=access_token,
                user_id=user_found.id,
                is_active=True,
                created_at=datetime.now(),
                updated_at=datetime.now(),
                deleted_at=None,
                expires_at=utils.get_expires_at(),
            ),
        )
        return Token(access_token=token_data.token, token_type="bearer")

    def verify_user(self, db: Session, token: str) -> Token:
        current_user = oauth2.get_current_user(db=db, token=token)
        self.__user_service.update_one_with_filter(
            db=db,
            filter={"email": current_user.email},
            user=UserUpdate(
                is_verified=True,
            ),
        )
        session_updated = self.__session_service.update_one_with_filter(
            db=db,
            filter={"token": token},
            session=SessionUpdate(expires_at=utils.get_expires_at()),
        )
        return Token(access_token=session_updated.token, token_type="bearer")

    async def create_session(self, db: Session, user_id: uuid.UUID):
        access_token = oauth2.create_access_token(data={"user_id": str(user_id)})
        session_created = self.__session_service.create(
            db=db,
            session=SessionCreate(
                token=access_token,
                user_id=user_id,
                is_active=True,
                created_at=datetime.now(),
                updated_at=datetime.now(),
                deleted_at=None,
                expires_at=utils.get_expires_at(),
            ),
        )
        return session_created

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
                session_created = await self.create_session(db, user_found.id)
                if not user_found.is_verified:
                    await self.__email_service.send_verification_email(
                        user_info, session_created.token
                    )
                    return RedirectResponse(
                        url="https://raw.githubusercontent.com/DNAnh01/assets/main/02.1.%20Sign%20up%20-%20Success.png"
                    )
                return Token(access_token=session_created.token, token_type="bearer")
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
                session_created = await self.create_session(db, new_user.id)
                await self.__email_service.send_verification_email(
                    user_info, session_created.token
                )
                return RedirectResponse(
                    url="https://raw.githubusercontent.com/DNAnh01/assets/main/02.1.%20Sign%20up%20-%20Success.png"
                )

    def sign_out(self, db: Session, token: str) -> Response:
        try:
            self.__session_service.remove_one_with_filter(
                db=db, filter={"token": token}
            )
            return JSONResponse(
                status_code=200, content={"message": "Sign out successful"}
            )
        except NoResultFound:
            logger.exception(
                f"Exception in {__name__}.{self.__class__.__name__}.sign_out: Invalid token: {token}"
            ),
            raise HTTPException(
                detail="Sign out failed: Invalid token",
            )

    async def forgot_password(self, db: Session, email: str) -> Response:
        user_found = self.__user_service.get_one_with_filter_or_none(
            db=db, filter={"email": email}
        )

        if user_found is None:
            logger.exception(
                f"Exception in {__name__}.{self.__class__.__name__}.forgot_password: User not found: {email}"
            )
            raise HTTPException(status_code=400, detail="User not found")

        session_created = await self.create_session(db=db, user_id=user_found.id)
        await self.__email_service.send_reset_password_email(
            email=user_found.email, token=session_created.token, db=db
        )
        return {"message": "Reset password email sent"}

    async def reset_password(self, db: Session, token: str) -> Token:
        session_found = self.__session_service.get_one_with_filter_or_none(
            db=db, filter={"token": token}
        )

        user_found = self.__user_service.get_one_with_filter_or_none(
            db=db, filter={"id": session_found.user_id}
        )

        if user_found is None:
            logger.exception(
                f"Exception in {__name__}.{self.__class__.__name__}.reset_password: User not found: {token}"
            )
            raise HTTPException(status_code=400, detail="User not found")

        reset_password = generate_random_string(32)

        self.__user_service.update_one_with_filter(
            db=db,
            filter={"id": user_found.id},
            user=UserUpdate(password_hash=utils.hash(reset_password), is_verified=True),
        )
        return Token(access_token=session_found.token, token_type="bearer")
