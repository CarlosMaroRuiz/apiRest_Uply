from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from src.bd.session import get_db
from src.user_auth.schemas.user_register import User_registrer
from src.user_auth.services.login_service import login_service
from src.user_auth.services.register_service import register_users

router_auth = APIRouter(prefix="/api/auth")

@router_auth.post("/register")
def register_user(register_data:User_registrer,db:Session = Depends(get_db)):
    return register_users(register_data,db)

@router_auth.get("/login")
def login(register_data:User_registrer,db:Session = Depends(get_db)):
    return login_service(register_data,db)