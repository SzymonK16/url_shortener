import time
import string
import uuid
from random import expovariate
from typing import Dict, Optional

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi.responses import RedirectResponse
from src.utils.encode_base64 import encode_base62
from src.schemas.urls_schema import *
from src.config.config import get_settings


url_router = APIRouter()

settings = get_settings()

lite_db: Dict[str, dict] = {}


@url_router.post("/short", response_model=UrlResponse)
async def get_links(request: UrlRequest):
    unique_id = uuid.uuid4().int >> 90
    short_id = encode_base62(unique_id)

    expires_in = int(time.time() + settings.URL_TIME)

    lite_db[short_id] = {
        "original_url": str(request.url),
        "expires_in": expires_in
    }

    return {
        "short_url": f"{settings.BASE_URL}/{short_id}",
        "expires_in": expires_in
    }

@url_router.get("/{short_url_id}")
async def redirect_to_original_url(short_url_id: str):
    data = lite_db.get(short_url_id)


    if time.time() > data["expires_in"]:
        del lite_db[short_url_id]
        raise HTTPException(status_code=410, detail="url expired")

    return RedirectResponse(url=data["original_url"])

