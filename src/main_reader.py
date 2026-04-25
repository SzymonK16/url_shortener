from fastapi import FastAPI
from src.api.routers.get_and_redirect_url import get_and_redirect_url

app = FastAPI()
app.include_router(get_and_redirect_url)