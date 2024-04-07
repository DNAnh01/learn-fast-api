import uuid
from datetime import datetime

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.common import utils
from app.common.logger import setup_logger
from app.core import oauth2
from app.crud.crud_user import crud_user
from app.models.user import User
from app.schemas.user import (UserCreate, UserInDB, UserOut, UserResetRequest,
                              UserUpdate)
from app.services.user_service import UserService

logger = setup_logger()

class UserServiceImpl(UserService):

    def __init__(self):
        self.__crud_user = crud_user

    def create(self, db: Session, user: UserCreate) -> UserOut:
        return self.__crud_user.create(db, obj_in=user)

    def get_by_id(self, db: Session, id: uuid.UUID) -> UserOut:
        return self.__crud_user.get_one_by_or_fail(db, {"id": id})

    def get_by_email_or_fail(self, db: Session, email: str) -> UserOut:
        return self.__crud_user.get_one_by_or_fail(db, {"email": email})

    def check_user_exists(self, db: Session, email: str) -> bool:
        try:
            self.__crud_user.get_one_by_or_fail(db, {"email": email})
            return True
        except:
            return False
        
    def get_details_by_email(self, db: Session, email: str) -> UserInDB:
        return self.__crud_user.get_one_by_or_fail(db, {"email": email})
        
    async def load_user(self, db: Session, email: str) -> UserInDB:
        try:
            user = self.get_details_by_email(db, email)
        except Exception as user_exec:
            logger.info(f"User not found, Email: {email}")
            user = None
        # if user.is_verified is False:
        #     raise HTTPException(status_code=400, detail="User is not verified")
        return user

    

    def update_is_verified(self, db: Session, email: str) -> UserOut:
        user = self.__crud_user.get_one_by_or_fail(db, {"email": email})
        return self.__crud_user.update(db, db_obj=user, obj_in={"is_verified": True})

    def update(self, db: Session, id: uuid.UUID, user: UserUpdate) -> UserOut:
        user_found = self.get_by_id(db, id)
        return self.__crud_user.update(db, db_obj=user_found, obj_in=user)
    
    async def load_user_by_token(self, db: Session, token: str) -> UserInDB:
        try:
            current_user = oauth2.get_current_user(db=db, token=token)
            user = self.get_details_by_email(db, current_user.email)
        except Exception as user_exec:
            logger.info(f"User not found, Token: {token}")
            user = None
        return user


    # async def reset_user_password(self, db: Session, data: UserResetRequest):
    #     user = await self.load_user(db, data.email)
    #     if not user:
    #         raise HTTPException(status_code=400, detail="User not found")
    #     if not user.is_verified:
    #         raise HTTPException(status_code=400, detail="User is not verified")
    #     if not user.is_active:
    #         raise HTTPException(status_code=400, detail="User is not active")
    #     user_token = user.get_context_string(EmailContextEnum.FORGOT_PASSWORD)

    #     try:
    #         token_valid = utils.verify(user_token, data.token)
    #     except Exception as verify_exec:
    #         logger.exception(f"Error verifying token: {verify_exec}")
    #         token_valid = False
    #     if not token_valid:
    #         raise HTTPException(status_code=400, detail="Invalid token")
        
    #     user.password = utils.hash(data.password)
    #     user.updated_at = datetime.now()
    #     self.__crud_user.update(db, db_obj=user, obj_in=user)