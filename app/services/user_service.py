import uuid
from abc import ABC, abstractmethod

from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserInDB, UserOut


class UserService(ABC):

    @abstractmethod
    def create(self, db: Session, user: UserCreate) -> UserOut:
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
    def update_is_verified(self, db: Session, email: str) -> UserOut:
        pass
