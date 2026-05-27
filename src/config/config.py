import os

from functools import lru_cache
from pydantic_settings import BaseSettings


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
ENV_PATH = os.path.join(BASE_DIR, ".env")


class Settings(BaseSettings):
    URL_TIME: int
    BASE_URL: str

    CASSANDRA_CLUSTER_NAME: str
    CASSANDRA_SNTCH: str
    CASSANDRA_DC: str
    CASSANDRA_SEEDS:str

    class Config:
        env_file = ENV_PATH


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    settings = Settings()
    return settings

