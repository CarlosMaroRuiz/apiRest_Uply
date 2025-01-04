from datetime import datetime, timedelta
from jose import jwt
from src.config import  Config

def create_access_token(data: dict):
    to_encode = data.copy()
    config = Config()

    if config.ACCESS_TOKEN_EXPIRE_MINUTES.lower() != "infinite":
        try:
            expire = datetime.utcnow() + timedelta(minutes=int(config.ACCESS_TOKEN_EXPIRE_MINUTES))
            to_encode.update({"exp": expire})
        except ValueError:
            raise ValueError("ACCESS_TOKEN_EXPIRE_MINUTES debe ser un numero o 'infinite'.")

    encoded_jwt = jwt.encode(to_encode,config.SECRET_KEY, algorithm=config.ALGORITHM)
    return encoded_jwt