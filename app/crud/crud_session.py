from app.crud.base import CRUDBase
from app.models.session import Session
from app.schemas.session import SessionCreate, SessionUpdate


class CRUDSession(CRUDBase[Session, SessionCreate, SessionUpdate]):
    pass


crud_session = CRUDSession(Session)
