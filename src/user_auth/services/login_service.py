from sqlalchemy.orm import Session
from src.bd.models.User_model import User
from src.shared.utils.jwt_utils import create_access_token
from src.user_auth.schemas.user_register import User_registrer
from src.shared.utils.hash import verify_password

def login_service(user_data:User_registrer,db:Session):
    user = db.query(User).filter(User.email == user_data.email).first()
    if user and verify_password(user_data.password, user.password):
        access_token = create_access_token({"sub": user.email})
        return {"message": "Login successful", "key": access_token}
    else:
        return {"message": "Invalid credentials"}