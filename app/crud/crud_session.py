

from app.crud.base import CRUDBase
from app.models.session import Session as SessionModel
from app.schemas.session import SessionCreate, SessionUpdate


class CRUDSession(CRUDBase[SessionModel, SessionCreate, SessionUpdate]):
    pass


crud_session = CRUDSession(SessionModel)
