from fastapi import FastAPI
from src.api.routers.post_url import post_url
from src.api.routers.get_and_redirect_url import get_and_redirect_url
from src.database.url_model import Base
from src.database.db_core import engine
app = FastAPI()
app.include_router(post_url)
app.include_router(get_and_redirect_url)

Base.metadata.create_all(engine)
