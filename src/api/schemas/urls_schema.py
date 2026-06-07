from pydantic import BaseModel,HttpUrl,field_validator


class UrlRequest(BaseModel):
    url: HttpUrl


class UrlResponse(BaseModel):
    short_url: str

    
