from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.common import utils
from app.core import oauth2
from app.schemas.session import SessionCreate
from app.schemas.token import Token
from app.schemas.user import UserCreate, UserLogin, UserOut
from app.services.auth_service import AuthService
from app.services.session_service_impl import SessionServiceImpl
from app.services.user_service_impl import UserServiceImpl


class AuthServiceImpl(AuthService):

    def __init__(self) -> None:
        self.__user_service = UserServiceImpl()
        self.__session_service = SessionServiceImpl()


    def sign_up(self, db: Session, user: UserCreate) -> UserOut:
        """
        Create a new user.
        Parameters:
        user (UserCreate): The user data to create a new user.
        db (Session): The database session.
        Returns:
        UserOut: The created user data.
        """
        # Hash the password
        hashed_password = utils.hash(user.password)
        user.password = hashed_password
        # Create the user using the user service
        new_user = self.__user_service.create(db=db, user=user)
        return new_user

    def sign_in(self, db: Session, user_credentials: UserLogin) -> Token:

        user = self.__user_service.get_by_email(db=db, email=user_credentials.email)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials"
            )

        if not utils.verify(user_credentials.password, user.password):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials"
            )
        access_token: str = oauth2.create_access_token(data={"user_id": str(user.id)})

        # Create a new session
        expires_at = utils.get_expires_at()
        new_session: SessionCreate = SessionCreate(token=access_token, 
                                                   user_id=user.id,
                                                   expires_at=expires_at)

        token_data = self.__session_service.create(db=db, session=new_session)

        return Token(access_token=token_data.token, token_type="bearer")