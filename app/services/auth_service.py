from abc import ABC, abstractmethod

from fastapi import Response
from sqlalchemy.orm import Session
from starlette.requests import Request

from app.schemas.token import Token
from app.schemas.user import UserCreate, UserLogin, UserOut


class AuthService(ABC):

    @abstractmethod
    def sign_up(self, db: Session, user: UserCreate) -> UserOut:
        pass

    @abstractmethod
    def sign_in(self, db: Session, user: UserLogin) -> Token:
        pass

    @abstractmethod
    async def verify_user(self, db: Session, token: str) -> Token:
        pass

    @abstractmethod
    async def handle_google_callback(self, request: Request, db: Session):
        pass

    @abstractmethod
    def sign_out(self, db: Session, token: str) -> Response:
        pass