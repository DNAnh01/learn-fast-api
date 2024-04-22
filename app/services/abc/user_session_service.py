from abc import ABC, abstractmethod
from typing import Optional

from sqlalchemy.orm import Session

from app.schemas.user_session import (UserSessionCreate, UserSessionOut,
                                      UserSessionUpdate)


class UserSessionService(ABC):

    @abstractmethod
    def create(self, db: Session, session: UserSessionCreate) -> UserSessionOut:
        pass

    @abstractmethod
    def get_one_with_filter_or_fail(self, db: Session, filter: dict) -> UserSessionOut:
        pass

    @abstractmethod
    def get_one_with_filter_or_none(
        self, db: Session, filter: dict
    ) -> Optional[UserSessionOut]:
        pass

    @abstractmethod
    def update_one_with_filter(
        self, db: Session, filter: dict, session: UserSessionUpdate
    ) -> UserSessionOut:
        pass

    @abstractmethod
    def remove_one_with_filter(self, db: Session, filter: dict) -> UserSessionOut:
        pass
