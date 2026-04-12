from fastapi import FastAPI
from src.routers.links import link_router
app = FastAPI()
app.include_router(link_router)