from fastapi_mail import FastMail, MessageSchema

from app.common.email_template import (
    email_forgot_password_template,
    email_verify_template,
)
from app.common.logger import setup_logger
from app.core.email_connection import conf

logger = setup_logger()


async def send_verification_email(
    user_info: dict, redirect_url: str, mode: int
) -> bool:
    """Send verification email to user."""
    fm = FastMail(conf)
    message = MessageSchema(
        subject="Verify Email Address for Sole Mate AI",
        recipients=[user_info["email"]],
        body=email_verify_template(
            user_name=user_info["name"],
            redirect_url=redirect_url,
            mode=mode,
        ),
        subtype="html",
    )
    try:
        await fm.send_message(message)
        return True
    except Exception as e:
        logger.error(f"Error in {__name__}.send_verification_email: {e}")
        return False


async def send_reset_password_email(
    email: str, password_reset: str, display_name: str
) -> bool:
    """Send reset password email to user."""
    fm = FastMail(conf)
    message = MessageSchema(
        subject="Reset Password for Sole Mate AI",
        recipients=[email],
        body=email_forgot_password_template(
            user_name=display_name,
            password_reset=password_reset,
        ),
        subtype="html",
    )
    try:
        await fm.send_message(message)
        return True
    except Exception as e:
        logger.error(f"Error in {__name__}.send_reset_password_email: {e}")
        return False