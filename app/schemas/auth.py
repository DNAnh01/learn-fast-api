from pydantic import BaseModel, EmailStr
import pydantic


class Email(BaseModel):

    email: EmailStr

class ChangePassword(BaseModel):
    password_old: str
    password_new: str

class EmailSchema(pydantic.BaseModel):
    email: pydantic.EmailStr