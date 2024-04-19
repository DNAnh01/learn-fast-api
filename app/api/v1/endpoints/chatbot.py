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
chatbot_service: ChatBotService = ChatBotServiceImpl(),



@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ChatBotOut)
def create(
    chatbot_create: ChatBotCreate,
    current_user_membership: UserSubscriptionPlan = Depends(oauth2.get_current_user_membership_info_by_token),
    db: Session = Depends(deps.get_db)
) -> ChatBotOut:
    
    """
        UserSubscriptionPlan(
            {
                "_Builder__u_id": "a7e47b5d-33c1-4cde-9176-be00b6319314",
                "_Builder__u_email": "donguyenanh2k1@gmail.com",
                "_Builder__us_expire_at": "2024-05-17 03:44:02.664871+07:00",
                "_Builder__sp_plan_title": "monthly_free",
                "_Builder__sp_plan_price": 0.0,
                "_Builder__sp_available_model": "GPT-3.5-Turbo LLM",
                "_Builder__sp_message_credits": 30,
                "_Builder__sp_number_of_chatbots": 1,
                "_Builder__sp_max_character_per_chatbot": 200000,
                "_Builder__sp_live_agent_takeover": false,
                "_Builder__sp_remove_label": false
            }
        )
    """
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


