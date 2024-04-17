from fastapi import APIRouter

from app.api.v1.endpoints import auth, brain

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["authentications"])
api_router.include_router(brain.router, prefix="/brain", tags=["brain"])
