import uuid
from abc import ABC, abstractmethod

from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserOut


class UserService(ABC):
    @abstractmethod
    def get(self, db: Session, id: uuid.UUID) -> UserOut:
        pass

    @abstractmethod
    def create(self, db: Session, user: UserCreate) -> UserOut:
        pass