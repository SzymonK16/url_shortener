from fastapi import FastAPI
from src.api.routers.post_url import post_url
from src.database.url_model import Base



app = FastAPI()
app.include_router(post_url)