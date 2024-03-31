import uuid
from datetime import datetime

from pydantic import BaseModel


class Auth(BaseModel):
    id: uuid.UUID
    email: str
    password: str
    created_at: datetime

    class Config:
        orm_mode = True
