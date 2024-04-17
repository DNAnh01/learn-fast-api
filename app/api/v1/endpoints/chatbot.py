from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from app.api import deps
from app.models.session import Session
from app.schemas.chatbot import ChatBotCreate, ChatBotUpdate, ChatBotOut
from app.services.chatbot_service_impl import ChatBotServiceImpl
from app.crud.crud_chatbot import crud_chatbot

router = APIRouter()

# auth_service = AuthServiceImpl()
chatbot_service = ChatBotServiceImpl()
# session_service = SessionServiceImpl()


# Below are routes for /chatbot


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ChatBotOut)
def create(
    token: str, chatbot_create: ChatBotCreate, db: Session = Depends(deps.get_db)
) -> ChatBotOut:
    new_brain = chatbot_service.create(db=db, chatbot=chatbot_create, token=token)
    return new_brain


@router.put(
    "/edit/{chatbot_id}", status_code=status.HTTP_200_OK, response_model=ChatBotOut
)
def update(
    token: str,
    chatbot_id: str,
    chatbot_update: ChatBotUpdate,
    db: Session = Depends(deps.get_db),
) -> ChatBotOut:
    existing_chatbot = chatbot_service.get(db, token=token, chatbot_id=chatbot_id)
    if not existing_chatbot:
        raise HTTPException(status_code=404, detail="Chatbot not found")
    updated_chatbot = crud_chatbot.update(
        db, db_obj=existing_chatbot, obj_in=chatbot_update
    )
    return updated_chatbot


@router.get(
    "/get/{chatbot_id}", status_code=status.HTTP_200_OK, response_model=ChatBotOut
)
def get(token: str, chatbot_id: str, db: Session = Depends(deps.get_db)) -> ChatBotOut:
    existing_chatbot = chatbot_service.get(db, token=token, chatbot_id=chatbot_id)
    if not existing_chatbot:
        raise HTTPException(status_code=404, detail="Chatbot not found")
    return existing_chatbot
