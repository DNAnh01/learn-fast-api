import uuid
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.common.utils import hash
from app.core.config import settings
from app.crud.crud_user import crud_user
from app.db.base_class import Base
from app.schemas.user import UserCreate
from app.services.user_service_impl import UserServiceImpl

user_service = UserServiceImpl()

engine = create_engine(
    f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_SERVER}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
)


def init_db():
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        # user = user_service.get_by_email(session, email="admin@admin.com")
        user = user_service.check_user_exists(session, email="admin@admin.com")
        if not user:
            user_in = UserCreate(
                id=uuid.uuid4(),
                email="admin@admin.com",
                password=hash("admin"),
                display_name="admin",
                avatar_url="https://raw.githubusercontent.com/DNAnh01/assets/main/default_user_avatar.png",
                created_at=datetime.now(),
                updated_at=datetime.now(),
                is_verified=False,
                user_role="admin",
                is_active=True,
                deleted_at=None,
            )
            user = crud_user.create(session, obj_in=user_in)
