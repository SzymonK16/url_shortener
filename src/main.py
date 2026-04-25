from fastapi import FastAPI
from src.routers.post_url import post_url
app = FastAPI()
app.include_router(post_url)