from fastapi import APIRouter
from app.api.v1.endpoints import chatbot
from app.api.v1.endpoints import auth

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["authentications"])
# api_router.include_router(subscription_plan.router, prefix="/subscription_plan", tags=["subscription_plans"])
api_router.include_router(chatbot.router, prefix="/chatbot", tags=["chatbot"])

