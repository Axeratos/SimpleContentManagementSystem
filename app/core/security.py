from uuid import uuid4

from jose import jwt
from passlib.context import CryptContext

from app.core.config import app_config

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ALGORITHM = "HS256"


def create_token():
    to_encode_data = {"subject": str(uuid4())}
    return jwt.encode(
        to_encode_data,
        app_config.JWT_SECRET_KEY,
        algorithm=ALGORITHM,
    )


def hash_password(plain_password: str):
    return pwd_context.hash(plain_password)


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)
