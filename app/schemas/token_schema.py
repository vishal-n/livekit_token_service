from pydantic import BaseModel
from typing import Optional


class TokenRequest(BaseModel):
    roomName: str
    participantId: str
    participantName: str
    avatarUrl: Optional[str] = None
    ttl: Optional[str] = "10m"
