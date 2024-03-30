from sqlalchemy.orm import Session

from app.core.security import get_password_hash
from app.crud import crud_user
from app.db.base_class import Base
from app.db.session import SessionLocal
from app.schemas.user import UserCreate


def init_db(db: Session) -> None:

    user = crud_user.get_by_email(db, email="admin@admin.com")
    if not user:
        user_in = UserCreate(
            email="admin@admin.com", password=get_password_hash(""), full_name="admin"
        )
        user = crud_user.create(db, obj_in=user_in)
