from typing import List

from pydantic import BaseModel, EmailStr


class EmailSchema(BaseModel):
    """
    Email schema
    """

    email: List[EmailStr]
