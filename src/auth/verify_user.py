from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer
from src.config import Config
from src.shared.utils.custom_exception import CustomAppException

config = Config()
oauth2_scheme_buyer = OAuth2PasswordBearer(tokenUrl="/api/auth/buyer")

def user_required(token: str = Depends(oauth2_scheme_buyer)):
    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=[config.ALGORITHM])
        return payload
    except JWTError:
        raise CustomAppException(
            code_error=401, msg="Token inválido"
        )
