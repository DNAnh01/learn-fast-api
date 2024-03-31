import uuid

from sqlalchemy.orm import Session

from app.crud.crud_user import crud_user
from app.schemas.user import UserCreate, UserOut
from app.services.user_service import UserService


class UserServiceImpl(UserService):

    def get(self, db: Session, id: uuid.UUID) -> UserOut:
        return crud_user.get(db, id)

    def create(self, db: Session, user: UserCreate) -> UserOut:
        return crud_user.create(db, obj_in=user)
