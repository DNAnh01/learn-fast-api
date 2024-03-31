from sqlalchemy import create_engine

from app.core.config import settings
from app.db.base_class import Base

engine = create_engine(
    f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_SERVER}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
)


def init_db():
    Base.metadata.create_all(engine)
