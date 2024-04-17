from abc import ABC, abstractmethod
from typing import Optional

from sqlalchemy.orm import Session

from app.schemas.session import SessionCreate, SessionOut, SessionUpdate


class SessionService(ABC):

    @abstractmethod
    def create(self, db: Session, session: SessionCreate) -> SessionOut:
        pass

    @abstractmethod
    def get_one_with_filter_or_fail(self, db: Session, filter: dict) -> SessionOut:
        pass

    @abstractmethod
    def get_one_with_filter_or_none(
        self, db: Session, filter: dict
    ) -> Optional[SessionOut]:
        pass

    @abstractmethod
    def update_one_with_filter(
        self, db: Session, filter: dict, session: SessionUpdate
    ) -> SessionOut:
        pass

    @abstractmethod
    def remove_one_with_filter(self, db: Session, filter: dict) -> SessionOut:
        pass
