import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    LIVEKIT_API_KEY = os.getenv("LIVEKIT_API_KEY")
    LIVEKIT_API_SECRET = os.getenv("LIVEKIT_API_SECRET")


settings = Settings()
