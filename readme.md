# 🚀 UPLY
## 🌟 Funcionalidades  
1. **Subida y clasificación de archivos**
2. **Cada usuario tiene su propio espacio de almacenamiento privado**
3. **Integrado con MinIO para un servidor de archivos de codigo abierto**
4. **Visualización y filtrado por categoria**
5. **Autenticacion JWT**

## 🛠️ Tecnologías utilizadas 
- **FastAPI**
- **MySQL**
- **MinIO**
## 🖥️ Cómo ejecutar el proyecto  
```bash  
git clone https://github.com/CarlosMaroRuiz/apiRest_Uply.git
```
Ejecutar los requirements del proyecto
```bash  
pip install -r requirements.txt  
```
Dentro de este proyecto se muestra un ejemplo de los parametros a ejecutar en el example.env y añadirlo en nuestro archivo .env

```.env
DATABASE_URL =
SECRET_KEY=
ALGORITHM=
ACCESS_TOKEN_EXPIRE_MINUTES=infinite
MINIO_ENDPOINT =
MINIO_ACCESS_KEY =
MINIO_SECRET_KEY= 
```
En el caso de querer instalar minio en un vps,maquina virtual en la nube se adjunta el siguiente enlace de pasos a seguir:
https://github.com/CarlosMaroRuiz/manualesLearn/blob/main/minio_e1.md
