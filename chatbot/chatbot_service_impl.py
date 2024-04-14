import uuid

from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.crud.crud_chatbot import crud_chatbot
from app.schemas.chatbot import ChatBotCreate, ChatBotUpdate, ChatBotOut
from app.services.chatbot_service import ChatBotService
from app.services.session_service_impl import SessionServiceImpl
from sqlalchemy.orm.exc import NoResultFound
from fastapi.responses import JSONResponse, RedirectResponse
from app.common.logger import setup_logger

logger = setup_logger()


class ChatBotServiceImpl(ChatBotService):

    def __init__(self):
        self.__crud_chatbot = crud_chatbot
        self.__session_service = SessionServiceImpl()

    def create(self, db: Session, chatbot: ChatBotCreate, token: str) -> ChatBotOut:
        try:
            sessionInfo = self.__session_service.get_one_with_filter_or_none(db=db, filter={"token": token})
            # Need to check user's current number of chatbots and user's tier to determine if user can create chat bot
            chatbot.user_id = sessionInfo.user_id
            return self.__crud_chatbot.create(db, obj_in=chatbot)
        except:
            logger.exception(
                f"Exception in {__name__}.{self.__class__.__name__}.create_chatbot: Invalid token: {token}"
            ),
            raise HTTPException(
                detail="Create Chatbot failed: Invalid token", status_code=401
            )

    def update(self, db: Session, brain: ChatBotUpdate) -> ChatBotOut:
        return self.__crud_chatbot.update(db, obj_in=brain)
