
import uuid
from abc import ABC, abstractmethod

from sqlalchemy.orm import Session

from app.schemas.session import SessionCreate, SessionOut, SessionUpdate


class SessionService:

    @abstractmethod
    def create(self, db: Session, session: SessionCreate) -> SessionOut:
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