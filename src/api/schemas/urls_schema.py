from pydantic import BaseModel,HttpUrl

class UrlRequest(BaseModel):
    url: HttpUrl


class UrlResponse(BaseModel):
    short_url: str
    expires_at: str
    
