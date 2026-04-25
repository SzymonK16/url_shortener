from fastapi import FastAPI
from src.api.routers.post_url import post_url
from src.database.url_model import Base
from src.database.db_core import engine

Base.metadata.create_all(engine)
app = FastAPI()
app.include_router(post_url)