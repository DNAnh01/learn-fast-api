from typing import Optional

from sqlalchemy.orm import Session

from fastapi import Depends, HTTPException
from fastapi.responses import JSONResponse, RedirectResponse

from app.schemas.user_subscription_plan import UserSubscriptionPlan
from app.common.logger import setup_logger
from app.common import utils
from app.crud.crud_user import crud_user
from app.schemas.user import (
    UserCreate,
    UserInDB,
    UserOut,
    UserSignInWithGoogle,
    UserUpdate,
    UpdatePassword,
)
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
            user_found = self.__crud_user.get_one_by_or_fail(
                db=db, filter=filter
            )
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

    def get_edit_one_with_filter_or_none(
        self, db: Session, filter: dict
    ) -> Optional[UserOut]:
        try:
            return self.__crud_user.get_one_by(db=db, filter=filter)
        except:
            logger.exception(
                f"Exception in {__name__}.{self.__class__.__name__}.get_edit_one_with_filter_or_none"
            )
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
        self,
        db: Session,
        filter: dict,
        user_update: UserUpdate,
        current_user_membership: UserSubscriptionPlan,
    ) -> UserOut:
        try:
            user = self.get_edit_one_with_filter_or_none(db=db, filter=filter)
            if user is None:
                logger.exception(
                    f"Exception in {__name__}.{self.__class__.__name__}.update_one_with_filter: user not found"
                )
                raise HTTPException(
                    detail="Update user failed: User not found",
                    status_code=404,
                )

            # Cập nhật thông tin người dùng
            updated_user = self.__crud_user.update(
                db=db, db_obj=user, obj_in=user_update
            )

            # Trả về thông tin người dùng sau khi cập nhật
            return updated_user
        except Exception as e:
            logger.exception(
                f"Exception in {__name__}.{self.__class__.__name__}.update_one_with_filter"
            )
            raise HTTPException(detail="Update user failed", status_code=400)

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
        return self.__crud_user.update(
            db, db_obj=user, obj_in={"is_verified": True}
        )

    def get_profile(
        self, db: Session, current_user_membership: UserSubscriptionPlan
    ) -> UserOut:
        user_found = self.__crud_user.get(
            db=db, id=current_user_membership.u_id
        )
        if user_found:
            result: UserOut = UserOut(**user_found.__dict__)
            return result
        return None

    async def change_password(
        self,
        db: Session,
        user_id: str,
        current_user_membership: UserSubscriptionPlan,
        password: UpdatePassword,
    ):
        user_found = self.__crud_user.get_one_by(
            db=db, filter={"id": current_user_membership.u_id}
        )
        if user_found is None:
            logger.error(
                f"Error in {__name__}.{self.__class__.__name__}.change_password: User not found"
            )
            return JSONResponse(
                status_code=404,
                content={"status": 404, "message": "User not found"},
            )
        if not utils.verify(password.password_old, user_found.password_hash):
            logger.error(
                f"Error in {__name__}.{self.__class__.__name__}.change_password: Old password is incorrect"
            )
            return JSONResponse(
                status_code=400,
                content={"status": 400, "message": "Old password is incorrect"},
            )
        user_updated = self.__crud_user.update_one_by(
            db=db,
            filter={"id": current_user_membership.u_id},
            obj_in={"password_hash": utils.hash(password.password_new)},
        )
        if user_updated is None:
            logger.error(
                f"Error in {__name__}.{self.__class__.__name__}.change_password: Change password failed"
            )
            return JSONResponse(
                status_code=500,
                content={"status": 500, "message": "Change password failed"},
            )
        return JSONResponse(
            status_code=200,
            content={"status": 200, "message": "Change password successful"},
        )
