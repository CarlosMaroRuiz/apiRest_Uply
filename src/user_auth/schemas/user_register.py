from pydantic import BaseModel, EmailStr

class User_registrer(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "usuario@gmail.com",
                "password": "contraseña_segura"
            }
        }
