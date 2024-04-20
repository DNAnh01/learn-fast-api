from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api import deps
from app.core import oauth2
from app.schemas.chatbot import ChatBotCreate, ChatBotOut, ChatBotUpdate
from app.schemas.user_subscription_plan import UserSubscriptionPlan
from app.services.chatbot_service import ChatBotService
from app.services.chatbot_service_impl import ChatBotServiceImpl

router = APIRouter()
chatbot_service: ChatBotService = ChatBotServiceImpl()



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




@router.get("/get_all", status_code=status.HTTP_200_OK, response_model=Optional[List[ChatBotOut]])
def get_all(
    current_user_membership: UserSubscriptionPlan = Depends(oauth2.get_current_user_membership_info_by_token),
    db: Session = Depends(deps.get_db)
) -> Optional[List[ChatBotOut]]:
    chatbots = chatbot_service.get_all_or_none(db=db, current_user_membership=current_user_membership)
    return chatbots


@router.get("/{chatbot_id}", status_code=status.HTTP_200_OK, response_model=Optional[ChatBotOut])
def get_one(
    chatbot_id: str,
    current_user_membership: UserSubscriptionPlan = Depends(oauth2.get_current_user_membership_info_by_token),
    db: Session = Depends(deps.get_db)
) -> Optional[ChatBotOut]:
    chatbot = chatbot_service.get_one_with_filter_or_none(db=db, current_user_membership=current_user_membership, filter={"id": chatbot_id})
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


