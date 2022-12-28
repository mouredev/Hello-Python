# Clase en vídeo (22/12/2022): https://www.twitch.tv/videos/1686104006

### User model ###

from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: Optional[str]
    username: str
    email: str
