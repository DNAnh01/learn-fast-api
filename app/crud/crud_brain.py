from app.crud.base import CRUDBase
from app.models.brain import Brain
from app.schemas.brain import BrainCreate, BrainUpdate


class CRUDBrain(CRUDBase[Brain, BrainCreate, BrainUpdate]):
    pass


crud_brain = CRUDBrain(Brain)
