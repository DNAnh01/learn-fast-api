import uuid

from sqlalchemy.orm import Session

from app.crud.crud_user import crud_user
from app.schemas.auth import Auth
from app.schemas.user import UserCreate, UserOut
from app.services.user_service import UserService


class UserServiceImpl(UserService):

    def create(self, db: Session, user: UserCreate) -> UserOut:
        return crud_user.create(db, obj_in=user)

    def get_by_id(self, db: Session, id: uuid.UUID) -> UserOut:
        return crud_user.get_one_by_or_fail(db, {"id": id})

    def get_by_email(self, db: Session, email: str) -> Auth:
        return crud_user.get_one_by_or_fail(db, {"email": email})
