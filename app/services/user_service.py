from abc import ABC, abstractmethod
from typing import Optional

from sqlalchemy.orm import Session

from app.schemas.user import (
    UserCreate,
    UserInDB,
    UserOut,
    UserSignInWithGoogle,
    UserUpdate,
)


class UserService(ABC):

    @abstractmethod
    def create(self, db: Session, user: UserCreate) -> UserOut:
        pass

    @abstractmethod
    def get_one_with_filter_or_fail(self, db: Session, filter: dict) -> UserOut:
        pass

    @abstractmethod
    def get_one_with_filter_or_none(
        self, db: Session, filter: dict
    ) -> Optional[UserOut]:
        pass

    @abstractmethod
    def get_one_with_filter_or_none(
        self, db: Session, filter: dict
    ) -> Optional[UserInDB]:
        pass

    @abstractmethod
    def update_one_with_filter(
        self, db: Session, filter: dict, user: UserUpdate
    ) -> UserOut:
        pass

    @abstractmethod
    def create_user_with_google(
        self, db: Session, user: UserSignInWithGoogle
    ) -> UserOut:
        pass

    @abstractmethod
    def update_is_verified(self, db: Session, email: str) -> UserOut:
        pass
