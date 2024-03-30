from sqlalchemy import Column, String

from app.db.base_class import Base


class User(Base):
    __tablename__ = "users"
    full_name = Column(String)
