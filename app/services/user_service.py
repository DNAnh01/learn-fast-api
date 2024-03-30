from abc import ABC, abstractmethod

from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate


class UserService(ABC):
    @abstractmethod
    def get(self, db: Session, id: int):
        pass

    @abstractmethod
    def create(self, db: Session, user: UserCreate) -> User:
        pass

    @abstractmethod
    def update(self, db: Session, id: int, user: UserUpdate):
        pass

    @abstractmethod
    def get_multi(self, db: Session, filter_param: str):
        pass
