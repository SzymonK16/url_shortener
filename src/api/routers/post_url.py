import uuid
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from src.database.db_core import get_db
from src.utils.encode_base64 import encode_base62
from src.api.schemas.urls_schema import UrlRequest, UrlResponse
from src.config.config import get_settings
from src.utils.expire_time import expire_time

post_url = APIRouter()
settings = get_settings()


@post_url.post("/short", response_model=UrlResponse)
def get_links(request: UrlRequest, db=Depends(get_db)):  # <- Usunięto 'async'

    unique_id = uuid.uuid4().int >> 90
    short_url = encode_base62(unique_id)

    now = datetime.now()

    expires_at = expire_time()

    ttl_seconds = int((expires_at - now).total_seconds())


    query = """
            INSERT INTO urls (short_url, original_url, created_at, last_used_at)
            VALUES (%s, %s, %s, %s)
            """

    db.execute(query, (short_url, str(request.url), now, now))

    return UrlResponse(
        short_url=f'{settings.BASE_URL}/{short_url}',
        expires_at=str(expires_at)
    )