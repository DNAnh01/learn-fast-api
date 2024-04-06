from datetime import datetime

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.session import Session as SessionModel
from app.schemas.session import SessionCreate, SessionUpdate


class CRUDSession(CRUDBase[SessionModel, SessionCreate, SessionUpdate]):
    def remove_by_token(self, db: Session, token: str) -> SessionModel:
        obj = db.query(self.model).filter(self.model.token == token).first()
        obj.deleted_at = datetime.now()
        db.add(obj)
        db.commit()
        return obj


crud_session = CRUDSession(SessionModel)
