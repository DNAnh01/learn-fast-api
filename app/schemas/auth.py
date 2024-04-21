from pydantic import BaseModel, EmailStr


class Email(BaseModel):

    email: EmailStr

class ChangePassword(BaseModel):
    password_old: str
    password_new: str
