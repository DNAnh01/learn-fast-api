import uuid
from abc import ABC, abstractmethod

from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate, UserGoogle, UserInDB, UserOut, UserUpdate


class UserService(ABC):

    @abstractmethod
    def create(self, db: Session, user: UserCreate) -> UserOut:
        pass

    @abstractmethod
    def create_user_with_google(self, db: Session, user: UserGoogle) -> UserOut:
        pass

    @abstractmethod
    def get_by_id(self, db: Session, id: uuid.UUID) -> UserOut:
        pass

    @abstractmethod
    def get_by_email_or_fail(self, db: Session, email: str) -> UserOut:
        pass

    @abstractmethod
    def check_user_exists(self, db: Session, email: str) -> bool:
        pass

    @abstractmethod
    def get_details_by_email(self, db: Session, email: str) -> UserInDB:
        pass

    @abstractmethod
    async def load_user(self, db: Session, email: str) -> User:
        pass

    @abstractmethod
    def update_is_verified(self, db: Session, email: str) -> UserOut:
        pass

    @abstractmethod
    def update(self, db: Session, id: uuid.UUID, user: UserUpdate) -> UserOut:
        pass

    @abstractmethod
    async def load_user_by_token(self, db: Session, token: str) -> UserInDB:
        pass
