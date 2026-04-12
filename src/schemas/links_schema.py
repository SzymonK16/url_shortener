from pydantic import BaseModel,HttpUrl

# class Link(BaseModel):
#     url: HttpUrl

class Link(BaseModel):
    url: str

