import datetime
from livekit.api import AccessToken, VideoGrants
from app.core.config import settings


def _parse_ttl(ttl_str: str) -> datetime.timedelta:
    """Parse TTL string (e.g. '10m', '1h', '60s') to timedelta."""
    if not ttl_str:
        return datetime.timedelta(minutes=10)
    ttl_str = ttl_str.strip().lower()
    if ttl_str.endswith("m"):
        return datetime.timedelta(minutes=int(ttl_str[:-1]))
    if ttl_str.endswith("h"):
        return datetime.timedelta(hours=int(ttl_str[:-1]))
    if ttl_str.endswith("s"):
        return datetime.timedelta(seconds=int(ttl_str[:-1]))
    return datetime.timedelta(minutes=10)


def generate_token(payload):
    custom_attributes = {}
    if payload.avatarUrl is not None:
        custom_attributes["avatarUrl"] = payload.avatarUrl

    token = (
        AccessToken(settings.LIVEKIT_API_KEY, settings.LIVEKIT_API_SECRET)
        .with_identity(str(payload.participantId))
        .with_name(payload.participantName)
        .with_ttl(_parse_ttl(payload.ttl or "10m"))
        .with_attributes(custom_attributes)
        .with_grants(
            VideoGrants(
                room_join=True,
                room=payload.roomName,
                can_publish=True,
                can_subscribe=True,
            )
        )
    )

    jwt = token.to_jwt()

    return {
        "success": True,
        "token": jwt,
        "roomName": payload.roomName,
        "participantId": payload.participantId,
        "participantName": payload.participantName,
        "expiresIn": payload.ttl
    }
