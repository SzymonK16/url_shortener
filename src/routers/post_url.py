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


post_url = APIRouter()

settings = get_settings()

lite_db: Dict[str, dict] = {}


@post_url.post("/short", response_model=UrlResponse)
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
