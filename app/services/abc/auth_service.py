from abc import ABC, abstractmethod
from typing import Union

from fastapi import Response
from sqlalchemy.orm import Session
from starlette.requests import Request

from app.schemas.auth import ChangePassword, Email
from app.schemas.token import Token
from app.schemas.user import UserOut, UserSignIn, UserSignUp

from app.schemas.auth import (
    EmailSchema,
)


class AuthService(ABC):

    @abstractmethod
    async def sign_up(self, db: Session, user: UserSignUp):
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
    def sign_out(self, db: Session, get_current_user: UserOut):
        pass

    @abstractmethod
    async def forgot_password(self, db: Session, email: EmailSchema):
        pass

    @abstractmethod
    async def change_password(
        self, db: Session, get_current_user: UserOut, password: ChangePassword
    ):
        pass
