from app.crud.base import CRUDBase
from app.models.user_session import UserSession
from app.schemas.user_session import UserSessionCreate, UserSessionUpdate


class CRUDUserSession(CRUDBase[UserSession, UserSessionCreate, UserSessionUpdate]):
    pass

crud_user_session = CRUDUserSession(UserSession)