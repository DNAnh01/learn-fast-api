from fastapi import APIRouter

from app.api.v1.endpoints import auth, chatbot, conversation

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth",
                          tags=["authentications"])
api_router.include_router(chatbot.router, prefix="/chatbot",
                          tags=["chatbots"])
api_router.include_router(conversation.router, prefix="/conversation",
                          tags=["conversations"])
