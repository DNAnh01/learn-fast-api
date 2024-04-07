import uuid

from sqlalchemy.orm import Session

from app.crud.crud_user import crud_user
from app.schemas.auth import Auth
from app.schemas.user import UserCreate, UserInDB, UserOut, UserUpdate
from app.services.user_service import UserService


class UserServiceImpl(UserService):

    def __init__(self):
        self.__crud_user = crud_user

    def create(self, db: Session, user: UserCreate) -> UserOut:
        print("IMPL")
        return self.__crud_user.create(db, obj_in=user)

    def get_by_id(self, db: Session, id: uuid.UUID) -> UserOut:
        return self.__crud_user.get_one_by_or_fail(db, {"id": id})

    def get_by_email_or_fail(self, db: Session, email: str) -> UserOut:
        return self.__crud_user.get_one_by_or_fail(db, {"email": email})

    def check_user_exists(self, db: Session, email: str) -> bool:
        try:
            self.__crud_user.get_one_by_or_fail(db, {"email": email})
            return True
        except:
            return False

    def get_details_by_email(self, db: Session, email: str) -> UserInDB:
        return self.__crud_user.get_one_by_or_fail(db, {"email": email})

    def update_is_verified(self, db: Session, email: str) -> UserOut:
        user = self.__crud_user.get_one_by_or_fail(db, {"email": email})
        return self.__crud_user.update(db, db_obj=user, obj_in={"is_verified": True})
