<<<<<<< HEAD
from typing import List, Optional

=======
import json
from typing import List, Optional

import requests
>>>>>>> origin/feature/MessageAndConversation
from fastapi import (APIRouter, Cookie, Depends, File, HTTPException, Request,
                     UploadFile, status)
from sqlalchemy.orm import Session

from app.api import deps
from app.core import oauth2
from app.schemas.chatbot import ChatBotCreate, ChatBotOut, ChatBotUpdate
from app.schemas.knowledge_base import (KnowledgeBaseAdd, KnowledgeBaseOut,
                                        KnowledgeBaseRemove)
<<<<<<< HEAD
from app.schemas.user_subscription_plan import UserSubscriptionPlan
from app.services.abc.chatbot_service import ChatBotService
from app.services.abc.knowledge_base_service import KnowledgeBaseService
from app.services.impl.chatbot_service_impl import ChatBotServiceImpl
from app.services.impl.knowledge_base_service_impl import \
    KnowledgeBaseServiceImpl

router = APIRouter()
chatbot_service: ChatBotService = ChatBotServiceImpl()
knowledge_base_service: KnowledgeBaseService = KnowledgeBaseServiceImpl()
=======
from app.schemas.conversation import (ConversationCreate,ConversationOut)
from app.schemas.user_subscription_plan import UserSubscriptionPlan
from app.services.abc.chatbot_service import ChatBotService
from app.services.abc.knowledgebase_service import KnowledgeBaseService
from app.services.impl.chatbot_service_impl import ChatBotServiceImpl
from app.services.impl.knowledgebase_service_impl import \
    KnowledgeBaseServiceImpl
from app.services.impl.conversation_service_impl import ConversationServiceImpl

router = APIRouter()
chatbot_service: ChatBotService = ChatBotServiceImpl()
conversation_service = ConversationServiceImpl()
knowledgebase_service: KnowledgeBaseService = KnowledgeBaseServiceImpl()
>>>>>>> origin/feature/MessageAndConversation



@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ChatBotOut)
def create(
    chatbot_create: ChatBotCreate,
    current_user_membership: UserSubscriptionPlan = Depends(oauth2.get_current_user_membership_info_by_token),
    db: Session = Depends(deps.get_db)
) -> ChatBotOut:
    chatbot_created: ChatBotOut = chatbot_service.create(
        db=db,
        chatbot_create=chatbot_create,
        current_user_membership=current_user_membership
    )
    return chatbot_created




@router.get("/get-all", status_code=status.HTTP_200_OK)
def get_all(
    current_user_membership: UserSubscriptionPlan = Depends(oauth2.get_current_user_membership_info_by_token),
    db: Session = Depends(deps.get_db)
):
    chatbots = chatbot_service.get_all_or_none(db=db, current_user_membership=current_user_membership)
    return chatbots


@router.get("/{chatbot_id}", status_code=status.HTTP_200_OK, response_model=Optional[ChatBotOut])
def get_one(
    chatbot_id: str,
    current_user_membership: UserSubscriptionPlan = Depends(oauth2.get_current_user_membership_info_by_token),
    db: Session = Depends(deps.get_db)
) -> Optional[ChatBotOut]:
<<<<<<< HEAD
    chatbot = chatbot_service.get_one_with_filter_or_none(db=db, current_user_membership=current_user_membership, filter={"id": chatbot_id})
=======
    chatbot = chatbot_service.get_one_with_filter_or_none(db=db, filter={"id": chatbot_id})
>>>>>>> origin/feature/MessageAndConversation
    if chatbot is None:
        raise HTTPException(status_code=404, detail="Chatbot not found")
    return chatbot


@router.put(
    "/edit/{chatbot_id}", status_code=status.HTTP_200_OK, response_model=ChatBotOut
)
def update(
    chatbot_id: str,
    chatbot_update: ChatBotUpdate,
    current_user_membership: UserSubscriptionPlan = Depends(oauth2.get_current_user_membership_info_by_token),
    db: Session = Depends(deps.get_db)
) -> ChatBotOut:
    updated_chatbot = chatbot_service.update_one_with_filter(db=db, chatbot_update=chatbot_update, current_user_membership=current_user_membership, filter={"id": chatbot_id})
    return updated_chatbot


@router.post("/{chatbot_id}/knowledge-base", status_code=status.HTTP_200_OK)
<<<<<<< HEAD
def add_knowledge_base(
=======
def add_knowledgeBase(
>>>>>>> origin/feature/MessageAndConversation
        chatbot_id: str,
        file: UploadFile = File(...),
        db: Session = Depends(deps.get_db)
):
    file_path = f"knowledge_files/{chatbot_id}_{file.filename}"
    with open(file_path, "wb") as f:
        f.write(file.file.read())
<<<<<<< HEAD
    created_knowledge_base = knowledge_base_service.create(db=db, chatbot_id=chatbot_id, file_path=file_path, file_name=file.filename)
    return created_knowledge_base
=======
    created_knowledgeBase = knowledgebase_service.create(db=db, chatbot_id=chatbot_id, file_path=file_path, file_name=file.filename)
    return created_knowledgeBase
>>>>>>> origin/feature/MessageAndConversation


@router.post("/{chatbot_id}/message", status_code=status.HTTP_200_OK)
def message_chatbot(
        chatbot_id: str,
        message: dict,
        request: Request,
        db: Session = Depends(deps.get_db),
<<<<<<< HEAD
        current_user_membership: UserSubscriptionPlan = Depends(oauth2.get_current_user_membership_info_by_token),
=======
>>>>>>> origin/feature/MessageAndConversation
        conversation_id: str = Cookie(None)
):
    # client_ip = request.client.host
    client_ip = "42.118.119.124"
<<<<<<< HEAD
    response = chatbot_service.message(db=db, chatbot_id=chatbot_id, conversation_id=conversation_id, current_user_membership=current_user_membership, message=message['message'], client_ip=client_ip)
    return response

=======
    response = chatbot_service.message(db=db, chatbot_id=chatbot_id, conversation_id=conversation_id, message=message['message'], client_ip=client_ip)
    return response


@router.get("/{chatbot_id}/new-conversation", status_code=status.HTTP_200_OK)
def new_conversation(
        chatbot_id: str,
        request: Request,
        db: Session = Depends(deps.get_db)
        ) -> ConversationOut:
    # client_ip = request.client.host
    client_ip = "42.118.119.124"
    new_conversation = conversation_service.create(
        db=db, chatbot_id=chatbot_id, client_ip=client_ip)
    return new_conversation
>>>>>>> origin/feature/MessageAndConversation
