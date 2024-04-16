from abc import ABC, abstractmethod

from fastapi import Response
from sqlalchemy.orm import Session
from starlette.requests import Request

from app.schemas.token import Token
from app.schemas.user import UserOut, UserSignIn, UserSignUp
from app.schemas.user_subscription_plan import UserSubscriptionPlan


class AuthService(ABC):

    @abstractmethod
    def sign_up(self, db: Session, user: UserSignUp) -> UserOut:
        pass

    @abstractmethod
    def sign_in(self, db: Session, user: UserSignIn) -> Token:
        pass

    @abstractmethod
    def verify_user(self, db: Session, token: str) -> Token:
        pass

    @abstractmethod
    def create_session(self, db: Session, user_id: str):
        pass

    @abstractmethod
    async def handle_google_callback(self, request: Request, db: Session):
        pass

    @abstractmethod
    def sign_out(self, db: Session, token: str) -> Response:
        pass

    @abstractmethod
    async def forgot_password(self, db: Session, email: str) -> Response:
        pass

    @abstractmethod
    async def reset_password(self, db: Session, token: str) -> Token:
        pass

    @abstractmethod
    def get_user_membership_info_by_token(self, db: Session, token: str) -> UserSubscriptionPlan:
        pass


