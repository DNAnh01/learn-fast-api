import uuid
from datetime import datetime

from sqlalchemy.orm import Session

from app.core import oauth2
from app.crud.crud_session import crud_session
from app.schemas.session import SessionCreate, SessionOut, SessionUpdate
from app.services.session_service import SessionService


class SessionServiceImpl(SessionService):

    def __init__(self, __crud_session=crud_session):
        self.__crud_session = __crud_session

    def create(self, db: Session, session: SessionCreate) -> SessionOut:
        return self.__crud_session.create(db, obj_in=session)

    def create_session(self, db: Session, user_id: str, expires_at: datetime):
        access_token: str = oauth2.create_access_token(data={"user_id": user_id})
        new_session: SessionCreate = SessionCreate(token=access_token, user_id=user_id, expires_at=expires_at)
        token_data = self.create(db=db, session=new_session)
        return token_data

    def get_by_id(self, db: Session, id: uuid.UUID) -> SessionOut:
        return self.__crud_session.get_one_by_or_fail(db, {"id": id})

    def get_by_token(self, db: Session, token: str) -> SessionOut:
        return self.__crud_session.get_one_by_or_fail(db, {"token": token})

    def update(self, db: Session, session: SessionUpdate) -> SessionOut:
        return self.__crud_session.update(db, obj_in=session)

    def update_expires_at(
        self, db: Session, token: str, expires_at: datetime
    ) -> SessionOut:
        session = self.__crud_session.get_one_by_or_fail(db, {"token": token})
        return self.__crud_session.update(
            db, db_obj=session, obj_in={"expires_at": expires_at}
        )
