import traceback
import uuid
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


    def create(self, db: Session, message: MessageCreate) -> MessageOut:
        """Create a new message."""
        try:
            return self.__crud_message.create(db, obj_in=message)
        except:
            logger.exception(
                f"Exception in {__name__}.{self.__class__.__name__}.create_message: Invalid token: {token}"
            ),
            raise HTTPException(
                detail="Create Message failed: Invalid token", status_code=401
            )

    def get_messages_by_conversation_id(self, db: Session, conversation_id: str) -> dict:
        """Get chat session messages"""
        try:
            conversation_id = uuid.UUID(conversation_id)
            messages = self.__crud_message.get_messages_by_conversation_id(
                db, conversation_id)
            # message_dicts = [MessageOut(**message.__dict__)
            #                  for message in messages]
            message_dicts = [dict(**message.__dict__)
                             for message in messages]
            # return MessageCollectionOut(messages=message_dicts)
            return message_dicts
        except:
            traceback.print_exc()
            pass

    def delete(self, db: Session, message_id: UUID, token: str):
        """Delete chat session messages"""
