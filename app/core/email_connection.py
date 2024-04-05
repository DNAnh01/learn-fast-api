from fastapi_mail import ConnectionConfig

from app.core.config import settings

conf = ConnectionConfig(
    MAIL_USERNAME=f"{settings.MAIL_USERNAME}",
    MAIL_PASSWORD=f"{settings.MAIL_PASSWORD}",
    MAIL_FROM=f"{settings.MAIL_FROM}",
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
)
