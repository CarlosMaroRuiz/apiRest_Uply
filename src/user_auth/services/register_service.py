from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from src.shared.utils.create_bucket import create_bucket_user
from src.shared.utils.custom_exception import CustomAppException
from src.bd.models.User_model import User
from src.shared.utils.hash import hash_password
from src.user_auth.schemas.user_register import User_registrer


def register_users(register_data:User_registrer,db:Session):
    try:
        user = User(**register_data.dict())
        user.password = hash_password(user.password)
        db.add(user)
        db.commit()
        db.refresh(user)
        create_bucket_user(user.email)
        return {"message": "User registered successfully", "user_email":register_data.email}
    except IntegrityError as e:
        db.rollback()
        return CustomAppException(400,"Email duplicated")
    except Exception as e:
        return CustomAppException(422,str(e))
