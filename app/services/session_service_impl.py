import uuid

from sqlalchemy.orm import Session

from app.crud.crud_session import crud_session
from app.schemas.session import SessionCreate, SessionOut, SessionUpdate
from app.services.session_service import SessionService


class SessionServiceImpl(SessionService):

    def __init__(self, __crud_session=crud_session):
        self.__crud_session = __crud_session

    def create(self, db: Session, session: SessionCreate) -> SessionOut:
        return self.__crud_session.create(db, obj_in=session)

    def get_by_id(self, db: Session, id: uuid.UUID) -> SessionOut:
        return self.__crud_session.get_one_by_or_fail(db, {"id": id})

    def get_by_token(self, db: Session, token: str) -> SessionOut:
        return self.__crud_session.get_one_by_or_fail(db, {"token": token})

    def update(self, db: Session, session: SessionUpdate) -> SessionOut:
        return self.__crud_session.update(db, obj_in=session)