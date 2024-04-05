from abc import ABC, abstractmethod


class EmailService(ABC):
    @abstractmethod
    async def send_verification_email(user_info: dict, access_token: str):
        pass