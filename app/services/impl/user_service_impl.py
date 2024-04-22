from typing import Optional

from sqlalchemy.orm import Session

from app.common.logger import setup_logger
from app.crud.crud_user import crud_user
from app.schemas.user import (UserCreate, UserInDB, UserOut,
                              UserSignInWithGoogle, UserUpdate)
from app.services.abc.user_service import UserService

logger = setup_logger()


class UserServiceImpl(UserService):

    def __init__(self):
        self.__crud_user = crud_user

    def create(self, db: Session, user: UserCreate) -> UserOut:
        user_found = self.get_one_with_filter_or_none(
            db=db, filter={"email": user.email}
        )
        if user_found is not None:
            raise Exception("User already exists")
        try:
            user_created = self.__crud_user.create(db=db, obj_in=user)
        except Exception as user_exec:
            logger.error(
                f"Error in {__name__}.{self.__class__.__name__}.create: {user_exec}"
            )
            raise user_exec
        if user_created:
            result: UserOut = UserOut(**user_created.__dict__)
        return result

    def get_one_with_filter_or_fail(self, db: Session, filter: dict) -> UserOut:
        try:
            user_found = self.__crud_user.get_one_by_or_fail(db=db, filter=filter)
        except Exception as user_exec:
            logger.error(
                f"Error in {__name__}.{self.__class__.__name__}.get_one_with_filter: {user_exec}"
            )
            raise user_exec
        if user_found:
            result: UserOut = UserOut(**user_found.__dict__)
        return result

    def get_one_with_filter_or_none(
        self, db: Session, filter: dict
    ) -> Optional[UserOut]:
        user_found = self.__crud_user.get_one_by(db=db, filter=filter)
        if user_found:
            result: UserOut = UserOut(**user_found.__dict__)
            return result
        return None

    def get_one_with_filter_or_none_db(
        self, db: Session, filter: dict
    ) -> Optional[UserInDB]:
        user_found = self.__crud_user.get_one_by(db=db, filter=filter)
        if user_found:
            result: UserInDB = UserInDB(**user_found.__dict__)
            return result
        return None

    def update_one_with_filter(
        self, db: Session, filter: dict, user: UserUpdate
    ) -> UserOut:
        try:
            user_updated = self.__crud_user.update_one_by(
                db=db, filter=filter, obj_in=user
            )
        except Exception as user_exec:
            logger.error(
                f"Error in {__name__}.{self.__class__.__name__}.update_one_with_filter: {user_exec}"
            )
            raise user_exec
        if user_updated:
            result: UserOut = UserOut(**user_updated.__dict__)
        return result

    def create_user_with_google(
        self, db: Session, user: UserSignInWithGoogle
    ) -> UserOut:
        user_found = self.get_one_with_filter_or_none(
            db=db, filter={"email": user.email}
        )

        if user_found is not None:
            return user_found

        try:
            user_created = self.__crud_user.create(
                db=db,
                obj_in=UserCreate(
                    email=user.email,
                    password_hash=user.password_hash,
                ),
            )
            user_updated = self.__crud_user.update_one_by(
                db=db,
                filter={"id": user_created.id},
                obj_in=UserUpdate(
                    email=user.email,
                    password_hash=user.password_hash,
                    display_name=user.display_name,
                    avatar_url=user.avatar_url,
                    is_verified=user.is_verified,
                    is_active=user.is_active,
                    created_at=user.created_at,
                    updated_at=user.updated_at,
                    deleted_at=user.deleted_at,
                    user_role=user.user_role,
                ),
            )
        except Exception as user_exec:
            logger.error(
                f"Error in {__name__}.{self.__class__.__name__}.create_user_with_google: {user_exec}"
            )
            raise user_exec
        if user_created:
            result: UserOut = UserOut(**user_updated.__dict__)
        return result

    def update_is_verified(self, db: Session, email: str) -> UserOut:
        user = self.__crud_user.get_one_by_or_fail(db, {"email": email})
        return self.__crud_user.update(db, db_obj=user, obj_in={"is_verified": True})

