import uuid
from datetime import datetime
from re import sub

from sqlalchemy import Boolean, Column, DateTime
from sqlalchemy.dialects.postgresql.base import UUID
from sqlalchemy.ext.declarative import as_declarative, declared_attr


# Function to convert CamelCase to snake_case
def snake_case(s):
    """
    e.g. "SnakeCase" -> "snake_case"
    e.g. "Snake-Case" -> "snake_case"
    e.g. "SNAKECase" -> "snake_case"
    e.g. "snakeCase" -> "snake_case"
    e.g. "SnakeCASE" -> "snake_case"
    """
    return "_".join(
        sub(
            "([A-Z][a-z]+)", r" \1", sub("([A-Z]+)", r" \1", s.replace("-", " "))
        ).split()
    ).lower()


# Base class for ORM models with common columns
@as_declarative()
class Base:
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = Column(DateTime(timezone=True), default=datetime.now)
    updated_at = Column(
        DateTime(timezone=True), default=datetime.now, onupdate=datetime.now
    )
    is_active = Column(Boolean, default=True)
    deleted_at = Column(DateTime(timezone=True), default=None)

    __name__: str

    # Generate __tablename__ automatically from class name
    @declared_attr
    def __tablename__(cls) -> str:
        return snake_case(cls.__name__)


# Base class for ORM models without common columns but with dynamic table name
@as_declarative()
class BaseMTM:
    """
    Base class for ORM models.
    """

    __name__: str

    # Generate __tablename__ automatically from class name
    @declared_attr
    def __tablename__(cls) -> str:
        return snake_case(cls.__name__)
