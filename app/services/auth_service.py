
from abc import ABC, abstractmethod

from sqlalchemy.orm import Session

from app.schemas.token import Token
from app.schemas.user import UserCreate, UserLogin, UserOut


class AuthService(ABC):

    @abstractmethod
    def sign_up(self, db: Session, user: UserCreate) -> UserOut:
        pass

    @abstractmethod
    def sign_in(self, db: Session, user: UserLogin) -> Token:
        pass