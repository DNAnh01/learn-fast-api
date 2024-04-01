import uuid

from sqlalchemy.orm import Session

from app.crud.crud_user import crud_user
from app.schemas.auth import Auth
from app.schemas.user import UserCreate, UserOut
from app.services.user_service import UserService


class UserServiceImpl(UserService):

    def __init__(self, __crud_user=crud_user):
        self.__crud_user = __crud_user


    def create(self, db: Session, user: UserCreate) -> UserOut:
        return self.__crud_user.create(db, obj_in=user)

    def get_by_id(self, db: Session, id: uuid.UUID) -> UserOut:
        return self.__crud_user.get_one_by_or_fail(db, {"id": id})

    def get_by_email(self, db: Session, email: str) -> Auth:
        return self.__crud_user.get_one_by_or_fail(db, {"email": email})
