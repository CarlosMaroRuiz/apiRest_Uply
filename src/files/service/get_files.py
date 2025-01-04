from typing import List

from src.files.utils.clasify_file_category import get_file_category
from src.shared.utils.create_bucket import generate_hash_from_email
from src.shared.utils.minio_client import client
from src.files.schemas.File import File_Schema
from typing import List, Optional


def get_file_user(current_user, category: Optional[str] = None) -> List[File_Schema]:
    bucket = generate_hash_from_email(current_user.get("sub"))
    objects = client.list_objects(bucket)

    files: List[File_Schema] = []
    for obj in objects:
        file_data = File_Schema(name=obj.object_name, size=obj.size, category=get_file_category(obj))
        if category:
            if file_data.category == category:
                files.append(file_data)
        else:
            files.append(file_data)

    return files
