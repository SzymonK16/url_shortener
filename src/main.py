from fastapi import FastAPI
from src.routers.urls import url_router
app = FastAPI()
app.include_router(url_router)