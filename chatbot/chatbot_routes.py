from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from starlette.requests import Request

from app.api import deps
from app.core.google_auth import oauth
from app.models.session import Session
from app.schemas.token import Token
from app.schemas.chatbot import ChatBotCreate, ChatBotUpdate, ChatBotOut
from app.services.auth_service_impl import AuthServiceImpl
from app.services.session_service_impl import SessionServiceImpl
from app.services.chatbot_service_impl import ChatBotServiceImpl

router = APIRouter()

# auth_service = AuthServiceImpl()
chatbot_service = ChatBotServiceImpl()
# session_service = SessionServiceImpl()


# Below are routes for /chatbot

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ChatBotOut)
def create(token: str, chatbot_create: ChatBotCreate, db: Session = Depends(deps.get_db)) -> ChatBotOut:
    new_brain = chatbot_service.create(db=db, chatbot=chatbot_create, token=token)
    return new_brain


@router.post("/edit", status_code=status.HTTP_200_OK, response_model=ChatBotOut)
def update(brain_update: ChatBotUpdate, db: Session = Depends(deps.get_db)) -> ChatBotOut:
    updated_brain = chatbot_service.update(db=db, brain=brain_update)
    return updated_brain

