import datetime
from sqlalchemy import Column, Integer, String, LargeBinary, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship


base = declarative_base()

class UrlModel(base):
    __tablename__ = 'urls'

    id = Column(Integer, primary_key=True)
    original_url = Column(String, index=True, nullable=False)
    short_url = Column(String, unique=True, index=True, nullable=False)
    created_at = Column(DateTime)
    expires_at = Column(DateTime)