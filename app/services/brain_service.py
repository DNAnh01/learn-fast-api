from abc import ABC, abstractmethod

from sqlalchemy.orm import Session

from app.schemas.brain import BrainCreate, BrainUpdate, BrainOut


class BrainService(ABC):

    @abstractmethod
    def create(self, db: Session, brain: BrainCreate) -> BrainOut:
        pass

    @abstractmethod
    def update(self, db: Session, brain: BrainUpdate) -> BrainOut:
        pass
