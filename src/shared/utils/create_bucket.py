import hashlib
from minio import S3Error
from src.shared.utils.minio_client import client

def generate_hash_from_email(email: str) -> str:

    hash_value = hashlib.sha256(email.encode('utf-8')).hexdigest()

    bucket_name = hash_value[:63]

    if bucket_name[0] in ['.', '-']:
        bucket_name = 'bucket-' + bucket_name[1:]
    if bucket_name[-1] in ['.', '-']:
        bucket_name = bucket_name[:-1] + '-bucket'

    return bucket_name


def create_bucket_user(email: str):
    try:
        bucket_name = generate_hash_from_email(email)

        if not client.bucket_exists(bucket_name):
            client.make_bucket(bucket_name)
            print(f"Bucket '{bucket_name}' creado con éxito.")
        else:
            print(f"El bucket '{bucket_name}' ya existe.")
    except S3Error as e:
        print(f"Error al crear el bucket: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
