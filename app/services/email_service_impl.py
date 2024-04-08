from fastapi_mail import FastMail, MessageSchema
from sqlalchemy.orm import Session

from app.common.email_template import (
    email_forgot_password_template,
    email_verify_template,
)
from app.core.email_connection import conf
from app.services.email_service import EmailService
from app.services.user_service_impl import UserServiceImpl


class EmailServiceImpl(EmailService):
    def __init__(self):
        self.__conf = conf
        self.__user_service = UserServiceImpl()

    async def send_verification_email(self, user_info: dict, access_token: str):
        fm = FastMail(self.__conf)
        message = MessageSchema(
            subject="Verify Email Address for Ally AI",
            recipients=[user_info["email"]],
            body=email_verify_template(user_info["name"], token=access_token),
            subtype="html",
        )
        await fm.send_message(message)

    async def send_reset_password_email(self, email: str, token: str, db: Session):
        # Load user information
        user_info = await self.__user_service.load_user(db=db, email=email)
        if not user_info:
            return {"message": "User not found"}

        user_name = user_info.display_name

        # Create FastMail instance
        fm = FastMail(self.__conf)

        # Create message
        message = MessageSchema(
            subject="Reset Password for Ally AI",
            recipients=[email],
            body=email_forgot_password_template(name=user_name, token=token),
            subtype="html",
        )

        # Send email
        await fm.send_message(message)
