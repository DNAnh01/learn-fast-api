import json
import traceback
from typing import List, Optional

import PyPDF2
from fastapi import Depends, HTTPException
from openai import OpenAI
from sqlalchemy.orm import Session

from app.common.logger import setup_logger
from app.crud.crud_chatbot import crud_chatbot
from app.schemas.chatbot import (ChatBotCreate, ChatBotInDB, ChatBotOut,
                                 ChatBotUpdate)
from app.schemas.user_subscription_plan import UserSubscriptionPlan
from app.services.chatbot_service import ChatBotService
from app.services.user_session_service import UserSessionService
from app.services.user_session_service_impl import UserSessionServiceImpl
from app.schemas.conversation import ConversationCreate,ConversationUpdate,ConversationOut
from app.schemas.message import MessageCreate,MessageUpdate,MessageOut,MessageBase
from app.crud.crud_conversation import crud_conversation
from app.crud.crud_message import crud_message
from app.services.conversation_service_impl import ConversationServiceImpl
from app.services.conversation_service import ConversationService
from app.services.message_service import MessageService
from app.services.message_service_impl import MessageServiceImpl
from app.crud.crud_message import crud_message
from app.services.knowledgeBase_service import KnowledgeBaseService
from app.core.config import settings

logger = setup_logger()

def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        text = ''
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

class ChatBotServiceImpl(ChatBotService):

    def __init__(self):
        self.__crud_chatbot = crud_chatbot
        self.__user_session_service: UserSessionService = UserSessionServiceImpl()
        self.__conversation_service: ConversationService = ConversationServiceImpl()
        self.__crud_message_base = crud_message
        self.__crud_message: MessageService = MessageServiceImpl()
        self.__crud_knowledgeBase = KnowledgeBaseService()
        self.client = OpenAI(api_key=settings.OPEN_API_KEY)
        self.DEFAULT_PROMPT = "You are a helpful assistant. The first prompt will be a long text," \
            "and any messages that you get be regarding that. Please answer any " \
            "questions and requests having in mind the first prompt"
        
    def create(self, db: Session, chatbot_create: ChatBotCreate, current_user_membership: UserSubscriptionPlan) -> ChatBotOut:
        # logger.warning(f"{current_user_membership}")
        logger.warning(f"{current_user_membership}")
        
        chatbots = self.get_all_or_none(db=db, current_user_membership=current_user_membership)
        if chatbots is not None and len(chatbots) >= current_user_membership.sp_number_of_chatbots:
            logger.exception(
                f"Exception in {__name__}.{self.__class__.__name__}.create_chatbot: User has reached the limit of chatbots"
            )
            raise HTTPException(
                detail="Create Chatbot failed: User has reached the limit of chatbots", status_code=400
            )
        chatbot_in_db: ChatBotInDB = ChatBotInDB(
                                **chatbot_create.__dict__, 
                                user_id=current_user_membership.u_id)
                                # prompt=self.DEFAULT_PROMPT)
        
        logger.info(f"ChatbotInDB: {chatbot_in_db}")

        try:
            chatbot_created = self.__crud_chatbot.create(db=db, obj_in=chatbot_in_db)
        except:
            logger.exception(
                f"Exception in {__name__}.{self.__class__.__name__}.create_chatbot"
            )
            raise HTTPException(
                detail="Create Chatbot failed", status_code=400
            )
        if chatbot_created:
            result: ChatBotOut = ChatBotOut(**chatbot_created.__dict__)
        return result


    def get_all_or_none(self, db: Session, current_user_membership: UserSubscriptionPlan) -> Optional[List[ChatBotOut]]:
        try:
            return self.__crud_chatbot.get_multi(db=db, filter_param={"user_id": current_user_membership.u_id})
        except:
            logger.exception(
                f"Exception in {__name__}.{self.__class__.__name__}.get_all_or_none"
            )
            return None
        

    def get_one_with_filter_or_none(self, db: Session, current_user_membership: UserSubscriptionPlan, filter: dict) -> Optional[ChatBotOut]:
        try:
            return self.__crud_chatbot.get_one_by(db=db, filter=filter)
        except:
            logger.exception(
                f"Exception in {__name__}.{self.__class__.__name__}.get_one_with_filter_or_none"
            )
            return None

    def update_one_with_filter(
        self, db: Session, chatbot_update: ChatBotUpdate, current_user_membership: UserSubscriptionPlan, filter: dict) -> ChatBotOut:
        try:
            chatbot = self.get_one_with_filter_or_none(db=db,                                   current_user_membership=current_user_membership, filter=filter)
            if chatbot is None:
                logger.exception(
                    f"Exception in {__name__}.{self.__class__.__name__}.update_one_with_filter: Chatbot not found"
                )
                raise HTTPException(
                    detail="Update Chatbot failed: Chatbot not found", status_code=404
                )
            return self.__crud_chatbot.update(db, obj_in=chatbot_update)
        except:
            logger.exception(
                f"Exception in {__name__}.{self.__class__.__name__}.update_one_with_filter"
            )
            raise HTTPException(
                detail="Update Chatbot failed", status_code=400
            )

    def message(
            self, db: Session, chatbot_id: str, conversation_id: str, message: str, current_user_membership: UserSubscriptionPlan, client_ip: str) -> MessageOut:
        try:
            conversation = self.__conversation_service.check_conversation(db=db, current_user_membership=current_user_membership, conversation_id=conversation_id, chatbot_id=chatbot_id, client_ip=client_ip)
            # Add message to Message
            message_form = {
                "sender_id": conversation.conversation_name,
                "sender_type": "guest",
                "message": message,
                "conversation_id": conversation.id
            }
            add_message = self.__crud_message_base.create(db=db, obj_in=message_form)
            # Handle response and add to Message
            response, chatbot_name = self.handle_message(db=db, chatbot_id=chatbot_id, conversation_id=conversation_id, message=message,current_user_membership=current_user_membership)
            message_form = {
                "sender_id": chatbot_name,
                "sender_type": "bot",
                "message": response,
                "conversation_id": conversation.id
            }
            add_message = self.__crud_message_base.create(db=db, obj_in=message_form)
            return add_message
        except:
            traceback.print_exc()
            pass

    def handle_message(
            self, db: Session, chatbot_id: str, conversation_id: str, message: str,
            current_user_membership: UserSubscriptionPlan):
        try:
            temp_knowledgeBase = []
            messages = self.__crud_message.get_messages_by_conversation_id(db=db, conversation_id=conversation_id)
            knowledgeBases = self.__crud_knowledgeBase.get_knowledgeBase_by_chatbot_id(db=db, chatbot_id=chatbot_id)
            chatbot = self.get_one_with_filter_or_none(db=db, current_user_membership=current_user_membership, filter={"id": chatbot_id})
            # Create response
            temp_knowledgeBase.append({'role': 'system', 'content': chatbot.prompt})
            for knowledgeBase in knowledgeBases:
                temp_knowledgeBase.append({'role': 'system', 'content': read_pdf(knowledgeBase['file_path'])})
            for message in messages:
                temp_knowledgeBase.append({'role': 'user', 'content': message['message']})
            response = self.client.chat.completions.create(
                model=chatbot.model,
                messages=temp_knowledgeBase
            )
            response = response.choices[0].message.content
            return response, chatbot.chatbot_name
        except:
            traceback.print_exc()
            pass