from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from uuid import UUID

from app.api import deps
from app.models.session import Session
from app.schemas.conversation import ConversationCreate, ConversationUpdate, ConversationOut
from app.services.conversation_service_impl import ConversationServiceImpl
from app.crud.crud_conversation import crud_conversation

router = APIRouter()

conversation_service = ConversationServiceImpl()


@router.post("/create-conversation", status_code=status.HTTP_201_CREATED, response_model=ConversationOut)
def create(token: str, conversation: ConversationCreate, chatbot_id: UUID, db: Session = Depends(deps.get_db)
           ) -> ConversationOut:
    new_conversation = conversation_service.create(
        db=db, conversation=conversation, chatbot_id=chatbot_id, token=token)
    return new_conversation


@router.post("/ask-question", status_code=status.HTTP_200_OK, response_model=str)
def ask_question(token: str, query: str, conversation_id: UUID, db: Session = Depends(deps.get_db)
                 ) -> str:
    respone = conversation_service.conversation(
        db, query, conversation_id, token)
    return respone


@router.post("/ask-question-with-streaming", status_code=status.HTTP_200_OK, response_model=str)
async def ask_question_with_streaming(token: str, query: str, conversation_id: UUID, db: Session = Depends(deps.get_db)) -> StreamingResponse:
    return StreamingResponse(conversation_service.conversation_with_streaming_request(db, query, conversation_id, token), media_type="text/event-stream")
