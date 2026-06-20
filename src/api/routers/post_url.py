import uuid
from datetime import datetime
from fastapi import APIRouter, Depends
from src.database.db_core import get_db
from src.utils.encode_base64 import encode_base62
from src.api.schemas.urls_schema import UrlRequest, UrlResponse
from src.config.config import get_settings
from src.services.url_word_list import check_word_in_url

post_url = APIRouter()
settings = get_settings()

insert_query = """
            INSERT INTO urls (short_url, original_url, created_at, last_used_at)
            VALUES (%s, %s, %s, %s)
            """

@post_url.post("/short", response_model=UrlResponse)
def get_links(request: UrlRequest, db=Depends(get_db)):
    unique_id = uuid.uuid4().int >> 90
    short_url = encode_base62(unique_id)
    now = datetime.now()

    check_word_in_url(str(request.url))

    query = insert_query
    db.execute(query, (short_url, str(request.url), now, now))


    return UrlResponse(
        short_url=f'{settings.REDIR_URL}/{short_url}'
    )