from fastapi import APIRouter
from app.schemas.token_schema import TokenRequest
from app.services.livekit_service import generate_token

router = APIRouter()


@router.post("/token")
async def create_livekit_token(payload: TokenRequest):
    return generate_token(payload)
