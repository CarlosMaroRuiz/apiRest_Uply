import os
import shutil
from tempfile import NamedTemporaryFile
from src.shared.utils.minio_client import client
from src.shared.utils.create_bucket import generate_hash_from_email

def upload_file_to_bucket(file, current_user):

    try:

        with NamedTemporaryFile(delete=False) as temp_file:
            shutil.copyfileobj(file.file, temp_file)
            temp_file.close()

            print(f"Archivo guardado temporalmente en {temp_file.name}")

            bucket_name = generate_hash_from_email(current_user.get("sub"))

            client.fput_object(bucket_name, file.filename, temp_file.name)
            print(f"Archivo subido al bucket '{bucket_name}' con éxito.")


            os.remove(temp_file.name)
            print(f"Archivo temporal {temp_file.name} eliminado.")

            return {"message": "Archivo subido exitosamente."}

    except Exception as e:

        if os.path.exists(temp_file.name):
            os.remove(temp_file.name)
        print(f"Error al cargar el archivo: {str(e)}")
        return {"error": f"Error al cargar el archivo: {str(e)}"}