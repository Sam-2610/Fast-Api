from fastapi import FastAPI
from pydantic import BaseModel
from . import models
from .database import engine
from .routers import user, post, auth


app = FastAPI()

models.Base.metadata.create_all(bind = engine)

class Post(BaseModel):
    title:str
    content:str
    published:bool = True
    
app.include_router(user.router)
app.include_router(post.router)
app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"Hello":"World"}





        