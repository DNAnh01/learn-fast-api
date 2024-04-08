from abc import ABC, abstractmethod

from sqlalchemy.orm import Session


class EmailService(ABC):
    @abstractmethod
    async def send_verification_email(user_info: dict, access_token: str):
        pass

    @abstractmethod
    async def send_reset_password_email(email: str, token: str, db: Session):
        pass
