
from sqlalchemy.orm import Session
from app.crud.crud_brain import crud_brain
from app.schemas.brain import BrainCreate, BrainUpdate, BrainOut
from app.services.brain_service import BrainService


class BrainServiceImpl(BrainService):

    def __init__(self):
        self.__crud_brain = crud_brain

    def create(self, db: Session, brain: BrainCreate) -> BrainOut:
        return self.__crud_brain.create(db, obj_in=brain)

    def update(self, db: Session, brain: BrainUpdate) -> BrainOut:
        return self.__crud_brain.update(db, obj_in=brain)
