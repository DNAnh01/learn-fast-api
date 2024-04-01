import uuid
from abc import ABC, abstractmethod

from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserOut


class UserService(ABC):

    @abstractmethod
    def create(self, db: Session, user: UserCreate) -> UserOut:
        pass

    @abstractmethod
    def get_by_id(self, db: Session, id: uuid.UUID) -> UserOut:
        pass

    @abstractmethod
    def get_by_email(self, db: Session, email: str) -> UserOut:
        pass
