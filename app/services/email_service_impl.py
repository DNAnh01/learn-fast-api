from fastapi_mail import ConnectionConfig, FastMail, MessageSchema

from app.common.email_template import email_template
from app.core.email_connection import conf
from app.services.email_service import EmailService


class EmailServiceImpl(EmailService):
    def __init__(self):
        self.__conf = conf


    async def send_verification_email(self, user_info: dict, access_token: str):
        fm = FastMail(self.__conf)
        message = MessageSchema(
            subject="Verify Email Address for Ally AI",
            recipients=[user_info["email"]],
            body=email_template(user_info["name"], token=access_token),
            subtype="html",
        )
        await fm.send_message(message)