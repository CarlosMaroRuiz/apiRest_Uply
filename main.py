from fastapi import FastAPI
from src.bd.models.base import Base
from src.bd.config_db import engine
from src.files.api_file import router_file
from src.shared.middlewares.exception_middleware import exception_middleware
from src.user_auth.api_users_auth import router_auth

app = FastAPI()
@app.on_event("startup")
async def startup_event():
    print("Creando tablas en la base de datos...")
    Base.metadata.create_all(bind=engine)

app.middleware("http")(exception_middleware)

#routes
app.include_router(router_auth)
app.include_router(router_file)