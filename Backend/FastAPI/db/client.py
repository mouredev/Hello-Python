# Clase en vídeo (22/12/2022): https://www.twitch.tv/videos/1686104006

### MongoDB client ###

# Descarga versión community: https://www.mongodb.com/try/download
# Instalación:https://www.mongodb.com/docs/manual/tutorial
# Módulo conexión MongoDB: pip install pymongo
# Ejecución: sudo mongod --dbpath "/path/a/la/base/de/datos/"
# Conexión: mongodb://localhost

from pymongo import MongoClient

# Descomentar el db_client local o remoto correspondiente

# Base de datos local MongoDB
db_client = MongoClient().local

# Clase en vídeo (28/12/2022): https://www.twitch.tv/videos/1691208894

# Base de datos remota MongoDB Atlas (https://mongodb.com)
# db_client = MongoClient(
#     "mongodb+srv://<user>:<password>@<url>/?retryWrites=true&w=majority").test

# Despliegue API en la nube:
# Deta - https://www.deta.sh/
# Intrucciones - https://fastapi.tiangolo.com/deployment/deta/
