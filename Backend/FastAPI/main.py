# Clase en vídeo (24/11/2022): https://www.twitch.tv/videos/1661716599

### Hola Mundo ###

# Documentación oficial: https://fastapi.tiangolo.com/es/

# Instala FastAPI: pip install "fastapi[all]"

from fastapi import FastAPI

app = FastAPI()

# Url local: http://127.0.0.1:8000
@app.get("/")
async def root():
    return "Hola FastAPI!"

# Url local: http://127.0.0.1:8000/url
@app.get("/url")
async def url():
    return { "url":"https://mouredev.com/python" }

# Inicia el server: uvicorn main:app --reload
# Detener el server: CTRL+C

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc