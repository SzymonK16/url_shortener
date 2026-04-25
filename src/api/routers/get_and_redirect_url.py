from fastapi import APIRouter,Depends
from sentry_sdk.session import Session
from src.database.db_core import get_db

get_and_redirect_url = APIRouter()

@get_and_redirect_url.get("/{short_url_id}")
async def redirect_to_original_url(db: Session = Depends(get_db())):
    pass
