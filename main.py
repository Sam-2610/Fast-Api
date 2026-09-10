from fastapi import FastAPI, HTTPException, status
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title:str
    content:str
    published:bool = True
    rating:Optional[int] = None
    

my_post = [{"title":"favorite food", "content":"I like Pizza", "id":2}]

@app.get("/")
def read_root():
    return {"Hello":"World"}

@app.get("/posts")
def get_posts():
    return {"data": my_post}

@app.post("/posts")
def create_post(post:Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_post.append(post_dict)
    print(post)
    return {"data": post_dict}

def find_post(id):
    for p in my_post:
        if p['id'] == id:
            return p

@app.get("/posts/{id}")
def get_post(id:int):
    post = find_post(id)
    print(id)
    return {"post_detail" : post}

def find_index(id):
    for i,p in enumerate(my_post):
        if p['id'] == id:
            return i

@app.delete("/posts/{id}",status_code=status.HTTP_202_ACCEPTED)
def delete_post(id:int):
    index = find_index(id)
    my_post.pop(index)
    return {"Message" : "Delete Sucessful"}

@app.put("/posts/{id}")
def update_post(id:int, post:Post):
    index = find_index(id)

    if index is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"post with {id} doesnt exist"
        )

    post_dict = post.dict()
    post_dict["id"] = id
    my_post[index] = post_dict

    return {"data" : post_dict}