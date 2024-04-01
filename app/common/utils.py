from datetime import datetime, timedelta
from typing import List

from passlib.context import CryptContext

from app.core.config import settings

# Create a CryptContext instance with bcrypt as the hashing scheme
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_expires_at() -> datetime:
    """
    Calculate the expiry time for an access token.

    This function gets the current time and adds the number of minutes specified in 
    settings.ACCESS_TOKEN_EXPIRE_MINUTES to it to calculate the expiry time.

    Returns:
    datetime: The datetime object representing the expiry time of the access token.
    """
    # Get the current time
    now = datetime.now()

    # Calculate the expiry time by adding the number of minutes specified in 
    # settings.ACCESS_TOKEN_EXPIRE_MINUTES to the current time
    expires_at = now + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    return expires_at

def hash(password: str) -> str:
    """
    Hash a password using the bcrypt scheme.

    Parameters:
    password (str): The password to be hashed.

    Returns:
    str: The hashed password.
    """
    return pwd_context.hash(password)


def verify(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a password against a hashed password.

    Parameters:
    plain_password (str): The plain text password to be verified.
    hashed_password (str): The hashed password to verify against.

    Returns:
    bool: True if the password matches the hashed password, False otherwise.
    """
    return pwd_context.verify(plain_password, hashed_password)


def pick_(source: any, keys: List[str]) -> dict:
    """
    This function tasks a source obj and a list of keys and return a new dictionary that includes only the keys present in the list.
    If the source is a dictionary, it directly fetches the values for the keys.
    If the source is not a dictionary, it treats it as an object and tries to fetch the attributes corresponding to the keys using getattr().
    """
    if type(source) is dict:
        return {key: source[key] for key in keys}

    return {key: getattr(source, key) for key in keys}


def clone_model(model):
    """
    Clone an arbitrary sqlalchemy model object without its primary key values.
    """
    # Ensure the model’s data is loaded before copying.
    model.id

    table = model.__table__
    non_pk_columns = [k for k in table.columns.keys() if k not in table.primary_key]
    data = {c: getattr(model, c) for c in non_pk_columns}
    if "id" in data:
        data.pop("id")
    return data
