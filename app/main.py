from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models
from .database import engine
from .routers import user, post, auth

app = FastAPI()

models.Base.metadata.create_all(bind = engine)

class Post(BaseModel):
    title:str
    content:str
    published:bool = True
    

while True:
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="new",
            user="postgres",
            password="2610",
            cursor_factory=RealDictCursor
        )
        cursor = conn.cursor()
        print("Database Connection was Sucessful!")
        break
    except Exception as error:
        print("Connection Failed", error)
        time.sleep(2)

app.include_router(user.router)
app.include_router(post.router)
app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"Hello":"World"}





        