from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello":"World"}

@app.get("/posts")
def get_posts():
    return {"data":"This is Your Post"}

@app.post("/createpost")
def create_post(payload:dict = Body(...)):
    print(payload)
    return {"message":"Sucessfully Created"}