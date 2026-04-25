import time
import uuid

from src.config.config import get_settings
from fastapi import APIRouter, Depends
from src.database.url_model import UrlModel
from src.utils.expire_time import expire_time
from sqlalchemy.orm.session import Session
from src.utils.encode_base64 import encode_base62
from src.api.schemas.urls_schema import *
from datetime import datetime
from src.database.db_core import get_db

post_url = APIRouter()
settings = get_settings()
@post_url.post("/short", response_model=UrlResponse)
async def get_links(request: UrlRequest, db: Session = Depends(get_db)):

    unique_id = uuid.uuid4().int >> 90
    short_url = encode_base62(unique_id)
    expires_at = expire_time()

    db_url = UrlModel(
        original_url=str(request.url),
        short_url=short_url,
        created_at=datetime.now(),
        expires_at=expires_at,
    )

    db.add(db_url)
    db.commit()
    db.refresh(db_url)

    return UrlResponse(
        short_url=f'{settings.BASE_URL}/{db_url.short_url}',
        expires_at=str(expires_at)
    )

