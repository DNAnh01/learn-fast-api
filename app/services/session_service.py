import uuid
from abc import ABC, abstractmethod
from datetime import datetime

from sqlalchemy.orm import Session

from app.schemas.session import SessionCreate, SessionOut, SessionUpdate


class SessionService:

    @abstractmethod
    def create(self, db: Session, session: SessionCreate) -> SessionOut:
        pass

    @abstractmethod
    def create_session(self,db: Session, user_id: str, expires_at: datetime):
        pass

    @abstractmethod
    def get_by_id(self, db: Session, id: uuid.UUID) -> SessionOut:
        pass

    @abstractmethod
    def get_by_token(self, db: Session, token: str) -> SessionOut:
        pass

    @abstractmethod
    def update(self, db: Session, session: SessionUpdate) -> SessionOut:
        pass

    @abstractmethod
    def update_expires_at(
        self, db: Session, token: str, expires_at: datetime
    ) -> SessionOut:
        pass
