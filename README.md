# LiveKit Token Service

A small FastAPI service that issues [LiveKit](https://livekit.io/) access tokens for joining rooms. Use it from your backend or frontend to authenticate participants without exposing your API secret.

## Requirements

- Python 3.9+
- A LiveKit server (cloud or self-hosted) and its API key and secret

## Setup

1. **Clone and enter the project**
   ```bash
   cd livekit_token_service
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install fastapi uvicorn python-dotenv
   ```

4. **Configure environment**
   Create a `.env` in the project root (see `.gitignore`; do not commit this file):
   ```env
   LIVEKIT_API_KEY=your_api_key
   LIVEKIT_API_SECRET=your_api_secret
   ```

## Run

```bash
python run.py
```

The API runs at **http://0.0.0.0:8000** with hot reload. Docs: **http://localhost:8000/docs**.

## API

### `POST /livekit/token`

Returns a JWT and metadata for a participant to join a LiveKit room.

**Request body (JSON)**

| Field            | Type   | Required | Description                          |
|------------------|--------|----------|--------------------------------------|
| `roomName`       | string | Yes      | LiveKit room name                    |
| `participantId`  | string | Yes      | Unique participant ID                |
| `participantName`| string | Yes      | Display name                         |
| `avatarUrl`      | string | No       | Avatar URL (stored in token metadata)|
| `ttl`            | string | No       | Token lifetime, e.g. `10m`, `1h`, `60s` (default: `10m`) |

**Example**

```bash
curl -X POST http://localhost:8000/livekit/token \
  -H "Content-Type: application/json" \
  -d '{
    "roomName": "my-room",
    "participantId": "user-123",
    "participantName": "Alice",
    "avatarUrl": "https://example.com/avatar.png",
    "ttl": "1h"
  }'
```

**Example response**

```json
{
  "success": true,
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "roomName": "my-room",
  "participantId": "user-123",
  "participantName": "Alice",
  "expiresIn": "1h"
}
```

Use the `token` value in your LiveKit client when connecting to the room.

## Project structure

```
livekit_token_service/
├── app/
│   ├── api/routes/   # API endpoints
│   ├── core/         # Config (env loading)
│   ├── schemas/      # Pydantic request/response models
│   └── services/     # LiveKit token generation
├── run.py            # Uvicorn entrypoint
├── requirements.txt
└── README.md
```

## License

Use and modify as needed for your project.
