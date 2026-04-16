from fastapi import APIRouter
from src.schemas.links_schema import Link
link_router = APIRouter()


@link_router.post("/links")
async def get_links(link: Link):
    return {"url": link.url}
