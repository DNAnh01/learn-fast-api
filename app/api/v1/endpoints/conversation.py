import uuid

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.api import deps
from app.core import oauth2
from app.schemas.conversation import ConversationCreate, ConversationOut
from app.schemas.user_subscription_plan import UserSubscriptionPlan
from app.services.conversation_service import ConversationService
from app.services.conversation_service_impl import ConversationServiceImpl

router = APIRouter()

conversation_service = ConversationServiceImpl()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ConversationOut)
def create(conversation: ConversationCreate,
            chatbot_id: uuid.UUID,
            db: Session = Depends(deps.get_db),
            conversation_service: ConversationService = Depends(),
            current_user_membership: UserSubscriptionPlan = Depends(oauth2.get_current_user_membership_info_by_token)
           ) -> ConversationOut:
    conversation_created = conversation_service.create(
        db=db,
        conversation_create=conversation,
        chatbot_id=chatbot_id,
        current_user_membership=current_user_membership)
    return conversation_created


@router.post("/create-conversation", status_code=status.HTTP_201_CREATED, response_model=ConversationOut)
def create(token: str, conversation: ConversationCreate, chatbot_id: uuid.UUID, db: Session = Depends(deps.get_db)
           ) -> ConversationOut:
    new_conversation = conversation_service.create(
        db=db, conversation=conversation, chatbot_id=chatbot_id, token=token)
    return new_conversation


@router.post("/ask-question", status_code=status.HTTP_200_OK, response_model=str)
def ask_question(token: str, query: str, conversation_id: uuid.UUID, db: Session = Depends(deps.get_db)
                 ) -> str:
    respone = conversation_service.conversation(
        db, query, conversation_id, token)
    return respone

