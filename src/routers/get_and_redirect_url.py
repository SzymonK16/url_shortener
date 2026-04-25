from fastapi import APIRouter



get_and_redirect_url = APIRouter()

@get_and_redirect_url.get("/{short_url_id}")
async def redirect_to_original_url(short_url_id: str):
    pass