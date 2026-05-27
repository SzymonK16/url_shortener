from fastapi import APIRouter, Depends, HTTPException
from datetime import datetime
from starlette.responses import RedirectResponse
from starlette.status import HTTP_404_NOT_FOUND
from src.database.db_core import get_db
get_and_redirect_url = APIRouter()

@get_and_redirect_url.get("/{short_url_id}")
def redirect_to_original_url(short_url_id: str, db=Depends(get_db)):


    query = "SELECT original_url FROM urls WHERE short_url = %s"
    row = db.execute(query, (short_url_id,)).one()

    if not row:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Bledny link lub link wygasl")

    now = datetime.now()
    update_query = "UPDATE urls SET last_used_at = %s WHERE short_url = %s"
    db.execute(update_query, (now, short_url_id))

    return RedirectResponse(url=row.original_url)