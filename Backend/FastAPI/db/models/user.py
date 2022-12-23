# Clase en vídeo (22/12/2022): https://www.twitch.tv/videos/1686104006

### User model ###

from pydantic import BaseModel


class User(BaseModel):
    id: str | None
    username: str
    email: str
