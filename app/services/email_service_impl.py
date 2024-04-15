from fastapi_mail import FastMail, MessageSchema
from sqlalchemy.orm import Session

from app.common.email_template import (
    email_forgot_password_template,
    email_verify_template,
)
from app.common.logger import setup_logger
from app.core.email_connection import conf
from app.schemas.user import UserOut
from app.services.email_service import EmailService
from app.services.user_service_impl import UserServiceImpl

logger = setup_logger()


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
        try:
            await fm.send_message(message)
            return True
        except Exception as e:
            logger.error(
                f"Error in {__name__}.{self.__class__.__name__}.send_verification_email: {e}"
            )
            return False

    async def send_reset_password_email(self, email: str, token: str, db: Session):
        user_info: UserOut = self.__user_service.get_one_with_filter_or_none(
            db=db, filter={"email": email}
        )
        user_name = user_info.display_name
        fm = FastMail(self.__conf)
        message = MessageSchema(
            subject="Reset Password for Ally AI",
            recipients=[email],
            body=email_forgot_password_template(name=user_name, token=token),
            subtype="html",
        )
        try:
            await fm.send_message(message)
            return True
        except Exception as e:
            logger.error(
                f"Error in {__name__}.{self.__class__.__name__}.send_reset_password_email: {e}"
            )
            return False
