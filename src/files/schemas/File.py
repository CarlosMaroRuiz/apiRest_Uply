from pydantic import BaseModel
from typing import Optional

class File_Schema(BaseModel):
    name: str
    size: int
    category: Optional[str] = None
