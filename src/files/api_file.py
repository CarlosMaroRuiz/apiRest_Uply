
from typing import List

from src.files.schemas.File import File_Schema
from src.files.service.get_files import get_file_user
from src.files.service.upload_file import upload_file_to_bucket
from fastapi import APIRouter, File, UploadFile, Depends
from src.auth.verify_user import user_required

router_file = APIRouter(prefix="/api/file")

@router_file.post("/")
async def upload_file(file: UploadFile = File(...), current_user: dict = Depends(user_required)):
    return upload_file_to_bucket(file, current_user)

@router_file.get("/files",response_model=List[File_Schema])
async def get_files(current_user: dict = Depends(user_required)):
    return get_file_user(current_user)

@router_file.get("/files/category/{category}", response_model=List[File_Schema])
async def get_files_by_category(category: str,current_user: dict = Depends(user_required)):
    return get_file_user(current_user, category)
