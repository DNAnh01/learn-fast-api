import json
from typing import List, Optional

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.common.logger import setup_logger
from app.crud.crud_chatbot import crud_chatbot
from app.schemas.chatbot import (ChatBotCreate, ChatBotInDB, ChatBotOut,
                                 ChatBotUpdate)
from app.schemas.user_subscription_plan import UserSubscriptionPlan
from app.services.chatbot_service import ChatBotService
from app.services.user_session_service import UserSessionService
from app.services.user_session_service_impl import UserSessionServiceImpl

logger = setup_logger()


class ChatBotServiceImpl(ChatBotService):

    def __init__(self):
        self.__crud_chatbot = crud_chatbot
        self.__user_session_service: UserSessionService = UserSessionServiceImpl()

        
        self.DEFAULT_PROMPT = "You are a helpful assistant. The first prompt will be a long text," \
            "and any messages that you get be regarding that. Please answer any " \
            "questions and requests having in mind the first prompt"
        
    def create(self, db: Session, chatbot_create: ChatBotCreate, current_user_membership: UserSubscriptionPlan) -> ChatBotOut:
        logger.warning(f"{current_user_membership}")
        logger.warning(f"{current_user_membership.sp_number_of_chatbots}")

        chatbots = self.get_all_or_none(db=db, current_user_membership=current_user_membership)


        if chatbots is not None and len(chatbots) >= current_user_membership['sp_number_of_chatbots']:
            logger.exception(
                f"Exception in {__name__}.{self.__class__.__name__}.create_chatbot: User has reached the limit of chatbots"
            )
            raise HTTPException(
                detail="Create Chatbot failed: User has reached the limit of chatbots", status_code=400
            )
        chatbot_in_db: ChatBotInDB = ChatBotInDB(
                                **chatbot_create.__dict__, 
                                user_id=current_user_membership['u_id'])
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
