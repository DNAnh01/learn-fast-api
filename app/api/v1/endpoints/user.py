from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.api import deps
from app.common import utils
from app.schemas.user import UserCreate, UserOut
from app.services.user_service import UserService
from app.services.user_service_impl import UserServiceImpl

router = APIRouter()
user_service: UserService = UserServiceImpl()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(deps.get_db)) -> UserOut:
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
    new_user = user_service.create(db=db, user=user)

    return new_user
