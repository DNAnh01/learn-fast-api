from typing import Optional

from sqlalchemy.orm import Session

from app.common import utils
from app.common.logger import setup_logger
from app.crud.crud_session import crud_session
from app.schemas.session import SessionCreate, SessionOut, SessionUpdate
from app.services.session_service import SessionService

logger = setup_logger()


class SessionServiceImpl(SessionService):

    def __init__(self):
        self.__crud_session = crud_session

    def create(self, db: Session, session: SessionCreate) -> SessionOut:
        session_found = self.get_one_with_filter_or_none(
            db=db, filter={"token": session.token}
        )
        if session_found is not None:
            return session_found
        try:
            session_created = self.__crud_session.create(db=db, obj_in=session)
        except Exception as session_exec:
            logger.error(
                f"Error in {__name__}.{self.__class__.__name__}.create: {session_exec}"
            )
            raise session_exec
        if session_created:
            result: SessionOut = SessionOut(**session_created.__dict__)
        return result

    def get_one_with_filter_or_fail(self, db: Session, filter: dict) -> SessionOut:
        try:
            session_found = self.__crud_session.get_one_by_or_fail(db=db, filter=filter)
        except Exception as session_exec:
            logger.error(
                f"Error in {__name__}.{self.__class__.__name__}.get_one_with_filter: {session_exec}"
            )
            raise session_exec
        if session_found:
            result: SessionOut = SessionOut(**session_found.__dict__)
        return result

    def get_one_with_filter_or_none(
        self, db: Session, filter: dict
    ) -> Optional[SessionOut]:
        session_found = self.__crud_session.get_one_by(db=db, filter=filter)
        if session_found:
            result: SessionOut = SessionOut(**session_found.__dict__)
            return result
        return None

    def update_one_with_filter(
        self, db: Session, filter: dict, session: SessionUpdate
    ) -> SessionOut:
        try:
            session_updated = self.__crud_session.update_one_by(
                db=db, filter=filter, obj_in=session
            )
        except Exception as session_exec:
            logger.error(
                f"Error in {__name__}.{self.__class__.__name__}.update_one_with_filter: {session_exec}"
            )
            raise session_exec
        if session_updated:
            result: SessionOut = SessionOut(**session_updated.__dict__)
        return result

    def remove_one_with_filter(self, db: Session, filter: dict) -> SessionOut:
        session_found = self.get_one_with_filter_or_none(db=db, filter=filter)
        if session_found is None:
            raise Exception(f"Session not found with filter: {filter}")
        try:
            session_removed = utils.asdict(
                self.__crud_session.remove(db=db, id=session_found.id)
            )

        except Exception as session_exec:
            logger.error(
                f"Error in {__name__}.{self.__class__.__name__}.remove_one_with_filter: {session_exec}"
            )
            raise session_exec
        if session_removed:
            result: SessionOut = SessionOut(**session_removed)
        return result