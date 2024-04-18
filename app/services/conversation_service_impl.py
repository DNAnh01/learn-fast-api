from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID
from typing import Generator, Any

from app.common.logger import setup_logger
from app.services.session_service_impl import SessionServiceImpl

from app.schemas.conversation import ConversationOut, ConversationCreate, ConversationUpdate
from app.services.conversation_service import ConversationService
from app.models.conversation import Conversation
from app.crud.crud_conversation import crud_conversation

from app.schemas.message import MessageCreate
from app.services.chatbot_service_impl import ChatBotServiceImpl
from app.services.message_service_imply import MessageServiceImpl

from openai import OpenAI
import PyPDF2
import datetime

from app.core.config import settings

logger = setup_logger()


class ConversationServiceImpl(ConversationService):

    def __init__(self):
        self.__crud_conversation = crud_conversation
        self.__chatbot_service = ChatBotServiceImpl()
        self.__message_service = MessageServiceImpl()
        self.__session_service = SessionServiceImpl()
        self.client = OpenAI(api_key=settings.OPEN_API_KEY)

    def create(self, db: Session, conversation: ConversationCreate, chatbot_id: UUID,  token: str) -> ConversationOut:
        try:
            sessionInfo = self.__session_service.get_one_with_filter_or_none(
                db=db, filter={"token": token}
            )

            conversation.chatbot_id = chatbot_id
            conversation.user_id = sessionInfo.user_id

            return self.__crud_conversation.create(db, obj_in=conversation)

        except:
            logger.exception(
                f"Exception in {__name__}.{self.__class__.__name__}.create_chatbot: Invalid token: {token}"
            ),
            raise HTTPException(
                detail="Create Conversation failed: Invalid token", status_code=401
            )

    # ask question
    def conversation(self, db: Session, query: str, conversation_id: UUID, token: str):
        """Get answer from the chat completation."""
        try:
            sessionInfo = self.__session_service.get_one_with_filter_or_none(
                db=db, filter={"token": token}
            )
            sent_at = datetime.datetime.now()

            conversation = self.__crud_conversation.get(db, id=conversation_id)

            chatbot = self.__chatbot_service.get(
                db=db, chatbot_id=conversation.chatbot_id, token=token
            )

            # Get chat history
            history = self.__message_service.get_messages_by_conversation_id(
                db=db, conversation_id=conversation_id, token=token)

            chat_history = []
            if history.messages:
                for message in history.messages:
                    chat_history.append(
                        {'role': 'user' if message.sender_type == "user" else 'system',
                         'content': message.message}
                    )

            # Add knowldege base
            knowledge_bases = {
                "path": "app\\services\\knowledge_files\\test.txt",
                "type": "txt"
            }
            if knowledge_bases["type"] == "pdf":
                with open(knowledge_bases["path"], "rb", encoding="utf-8") as file:
                    pdf = PyPDF2.PdfFileReader(file)
                    for page_num in range(pdf.getNumPages()):
                        page = pdf.getPage(page_num)
                        chat_history.append(
                            {'role': 'user',
                             'content': page.extractText()}
                        )
            else:
                with open(knowledge_bases["path"], "r", encoding="utf-8") as file:
                    chat_history.append(
                        {'role': 'user',
                         'content': file.read()}
                    )

            # Add user query
            chat_history.append(
                {'role': 'user',
                 'content': query}
            )

            # Create Response
            response = self.client.chat.completions.create(
                model=chatbot.model,
                temperature=chatbot.temperature,
                max_tokens=chatbot.max_tokens,
                messages=chat_history
            )

            self.__message_service.create(
                db=db,
                message=MessageCreate(
                    conversation_id=conversation_id,
                    sender_id=sessionInfo.user_id,
                    sender_type="user",
                    message=query,
                    sent_at=sent_at
                ),
                token=token
            )

            self.__message_service.create(
                db=db,
                message=MessageCreate(
                    conversation_id=conversation_id,
                    sender_id=chatbot.id,
                    sender_type="system",
                    message=response.choices[0].message.content,
                    sent_at=sent_at
                ),
                token=token
            )

            return response.choices[0].message.content
        except Exception as e:
            logger.exception(
                f"Exception in {__name__}.{self.__class__.__name__}.Conversation: {str(e)}"
            ),
            raise HTTPException(
                detail="Conversation failed: An error occurred", status_code=500
            )

    def conversation_with_streaming_request(self, db: Session, query: str, conversation_id: UUID, token: str) -> Generator[Any, None, None]:
        """Get answer from the chat completation."""
        try:
            sessionInfo = self.__session_service.get_one_with_filter_or_none(
                db=db, filter={"token": token}
            )
            sent_at = datetime.datetime.now()

            conversation = self.__crud_conversation.get(db, id=conversation_id)

            chatbot = self.__chatbot_service.get(
                db=db, chatbot_id=conversation.chatbot_id, token=token
            )

            # Get chat history
            history = self.__message_service.get_messages_by_conversation_id(
                db=db, conversation_id=conversation_id, token=token)

            chat_history = []
            if history.messages:
                for message in history.messages:
                    chat_history.append(
                        {'role': 'user' if message.sender_type == "user" else 'system',
                         'content': message.message}
                    )

            # Add knowldege base
            knowledge_bases = {
                "path": "app\\services\\knowledge_files\\test.txt",
                "type": "txt"
            }
            if knowledge_bases["type"] == "pdf":
                with open(knowledge_bases["path"], "rb", encoding="utf-8") as file:
                    pdf = PyPDF2.PdfFileReader(file)
                    for page_num in range(pdf.getNumPages()):
                        page = pdf.getPage(page_num)
                        chat_history.append(
                            {'role': 'user',
                             'content': page.extractText()}
                        )
            else:
                with open(knowledge_bases["path"], "r", encoding="utf-8") as file:
                    chat_history.append(
                        {'role': 'user',
                         'content': file.read()}
                    )

            # Add user query
            chat_history.append(
                {'role': 'user',
                 'content': query}
            )

            # Create Response
            response_stream = self.client.chat.completions.create(
                model=chatbot.model,
                temperature=chatbot.temperature,
                max_tokens=chatbot.max_tokens,
                messages=chat_history,
                stream=True,
            )

            complete_respone = ""
            # Yield each chunk of the response as it becomes available
            for respone_chunk in response_stream:
                if respone_chunk.choices[0].delta.content is not None:
                    content = respone_chunk.choices[0].delta.content
                    yield content
                    complete_respone += content

            self.__message_service.create(
                db=db,
                message=MessageCreate(
                    conversation_id=conversation_id,
                    sender_id=sessionInfo.user_id,
                    sender_type="user",
                    message=query,
                    sent_at=sent_at,
                ),
                token=token
            )

            self.__message_service.create(
                db=db,
                message=MessageCreate(
                    conversation_id=conversation_id,
                    sender_id=sessionInfo.user_id,
                    sender_type="system",
                    message=complete_respone,
                    sent_at=datetime.datetime.now(),
                ),
                token=token
            )

        except Exception as e:
            logger.exception(
                f"Exception in {__name__}.{self.__class__.__name__}.Conversation: {str(e)}"
            ),
            raise HTTPException(
                detail="Conversation failed: An error occurred", status_code=500
            )
