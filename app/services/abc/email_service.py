from abc import ABC, abstractmethod

from sqlalchemy.orm import Session


class EmailService(ABC):
    @abstractmethod
    async def send_verification_email(self, user_info: dict, redirect_url: str) -> bool:
        pass

    @abstractmethod
    async def send_reset_password_email(self, email: str, password_reset: str, db: Session) -> bool:
        pass
