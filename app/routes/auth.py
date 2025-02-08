from fastapi import HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
from app.config import API_KEY

api_key_header = APIKeyHeader(name="X-API-KEY")

def validate_api_key(api_key: str = Security(api_key_header)):
    if api_key is None or api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing API key",
        )
    return None