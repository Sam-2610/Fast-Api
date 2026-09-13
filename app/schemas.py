from pydantic import BaseModel, EmailStr
from datetime import datetime


class PostBase(BaseModel):
    title:str
    content:str
    published:bool = True

class CreatePost(PostBase):
    pass

class Usercreate(BaseModel):
    email:EmailStr
    password:str

class PostResponse(PostBase):
    id:int
    created_at:datetime

    class Config:
        from_attributes = True

class Userout(BaseModel):
    id:int
    email:EmailStr

    class Config:
        from_attributes = True

class Userlogin(BaseModel):
    email:EmailStr
    password:str

   