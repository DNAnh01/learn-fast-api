from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from starlette.requests import Request

from app.api import deps
from app.core.google_auth import oauth
from app.models.session import Session
from app.schemas.token import Token
from app.schemas.brain import BrainCreate, BrainUpdate, BrainOut
from app.services.auth_service_impl import AuthServiceImpl
from app.services.session_service_impl import SessionServiceImpl
from app.services.brain_service_impl import BrainServiceImpl

router = APIRouter()

# auth_service = AuthServiceImpl()
brain_service = BrainServiceImpl()
# session_service = SessionServiceImpl()



@router.post("/", status_code=status.HTTP_201_CREATED, response_model=BrainOut)
def create(brain_create: BrainCreate, db: Session = Depends(deps.get_db)) -> BrainOut:
    new_brain = brain_service.create(db=db, brain=brain_create)
    return new_brain


@router.post("/edit", status_code=status.HTTP_200_OK, response_model=BrainOut)
def update(brain_update: BrainUpdate, db: Session = Depends(deps.get_db)) -> BrainOut:
    updated_brain = brain_service.update(db=db, brain=brain_update)
    return updated_brain

