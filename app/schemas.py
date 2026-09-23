from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class PostBase(BaseModel):
    title:str
    content:str
    published:bool = True
    
    

class CreatePost(PostBase):
    pass

class Usercreate(BaseModel):
    email:EmailStr
    password:str

class Userout(BaseModel):
    id:int
    email:EmailStr
    

    class Config:
        from_attributes = True


class PostResponse(PostBase):
    id:int
    created_at:datetime
    user_id:int
    user:Userout
   
    
    

    class Config:
        from_attributes = True


class Userlogin(BaseModel):
    email:EmailStr
    password:str

class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    id:Optional[str] = None

   