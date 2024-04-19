from uuid import UUID

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.common.logger import setup_logger
from app.crud.crud_message import crud_message
from app.schemas.message import MessageCollectionOut, MessageCreate, MessageOut
from app.services.message_service import MessageService
from app.services.user_session_service import UserSessionService
from app.services.user_session_service_impl import UserSessionServiceImpl

logger = setup_logger()


class MessageServiceImpl(MessageService):

    def __init__(self):
        self.__crud_message = crud_message
        self.__user_session_service:UserSessionService = UserSessionServiceImpl()


    # def create(self, db: Session, message: MessageCreate, token: str) -> MessageOut:
    #     """Create a new message."""

    #     try:
    #         sessionInfo = self.__session_service.get_one_with_filter_or_none(
    #             db=db, filter={"token": token}
    #         )
    #         return self.__crud_message.create(db, obj_in=message)
    #     except:
    #         logger.exception(
    #             f"Exception in {__name__}.{self.__class__.__name__}.create_message: Invalid token: {token}"
    #         ),
    #         raise HTTPException(
    #             detail="Create Message failed: Invalid token", status_code=401
    #         )

    # def get_messages_by_conversation_id(self, db: Session, conversation_id: str, token: str) -> MessageCollectionOut:
    #     """Get chat session messages"""
    #     try:
    #         sessionInfo = self.__session_service.get_one_with_filter_or_none(
    #             db=db, filter={"token": token}
    #         )
    #         messages = self.__crud_message.get_messages_by_conversation_id(
    #             db, conversation_id)
    #         print(messages)
    #         message_dicts = [MessageOut(**message.__dict__)
    #                          for message in messages]
    #         return MessageCollectionOut(messages=message_dicts)
    #     except:
    #         logger.exception(
    #             f"Exception in {__name__}.{self.__class__.__name__}.get_message: Invalid token: {token}"
    #         ),
    #         raise HTTPException(
    #             detail="Get Message failed: Invalid token", status_code=401
    #         )

    # def delete(self, db: Session, message_id: UUID, token: str):
    #     """Delete chat session messages"""
