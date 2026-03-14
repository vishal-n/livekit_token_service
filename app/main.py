from fastapi import FastAPI
from app.api.routes.token_routes import router as token_router

app = FastAPI(title="LiveKit Token Service")

app.include_router(token_router, prefix="/livekit", tags=["LiveKit"])
