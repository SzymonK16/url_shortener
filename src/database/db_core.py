from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.config.config import get_settings

settings = get_settings()
db_user = settings.POSTGRES_USER
db_password = settings.POSTGRES_PASSWORD
db_name = settings.POSTGRES_DB

engine = create_engine(f'postgresql+psycopg2://{db_user}:{db_password}@database:5432/{db_name}')

SessionLocal = sessionmaker(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
