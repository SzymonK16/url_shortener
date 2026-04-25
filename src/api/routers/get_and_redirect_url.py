from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sentry_sdk.session import Session
from starlette.responses import RedirectResponse
from starlette.status import HTTP_404_NOT_FOUND

from src.database.db_core import get_db
from src.database.url_model import UrlModel
from src.utils.expire_time import expire_time

get_and_redirect_url = APIRouter()

@get_and_redirect_url.get("/{short_url_id}")
async def redirect_to_original_url(short_url_id: str,db: Session = Depends(get_db)):
    db_url = db.query(UrlModel).filter(UrlModel.short_url == short_url_id).first()

    if not db_url:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND)

    expiry_date = db_url.expires_at
    if expiry_date and expiry_date < datetime.now():
        db.delete(db_url)
        db.commit()
        raise HTTPException(status_code=410, detail="Link has expired")


    return RedirectResponse(url=db_url.original_url)

