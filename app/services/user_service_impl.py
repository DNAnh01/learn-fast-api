from typing import Optional

from sqlalchemy.orm import Session

from app.crud.crud_user import crud_user
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.services.user_service import UserService


class UserServiceImpl(UserService):
    def get(self, db: Session, id: int):
        return crud_user.get(db, id)

    def create(self, db: Session, user: UserCreate) -> User:
        return crud_user.create(db, obj_in=user)

    def update(self, db: Session, id: int, user: UserUpdate):
        return crud_user.update(db, id, user)

    def get_multi(self, db: Session, filter_param: str):
        return crud_user.get_multi(db, filter_param)
