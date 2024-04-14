from app.crud.base import CRUDBase
from app.models.chatbot import ChatBot
from app.schemas.chatbot import ChatBotCreate, ChatBotUpdate


class CRUDChatBot(CRUDBase[ChatBot, ChatBotCreate, ChatBotUpdate]):
    pass


crud_chatbot = CRUDChatBot(ChatBot)
