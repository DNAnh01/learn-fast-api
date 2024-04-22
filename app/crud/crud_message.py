from app.crud.base import CRUDBase
from app.models.message import Message
from app.schemas.message import MessageCreate, MessageUpdate
from sqlalchemy.orm import Session
from sqlalchemy import asc

import uuid as UUID


class CRUDMessage(CRUDBase[Message, MessageCreate, MessageUpdate]):
    # Add a method to get messages by conversation_id
    def get_messages_by_conversation_id(self, db: Session, conversation_id: UUID):
        result = (db.query(Message)
                .filter(Message.conversation_id == conversation_id)
                .filter(Message.deleted_at == None)
                .order_by(asc(Message.created_at))
                .all())
        return result


crud_message = CRUDMessage(Message)
