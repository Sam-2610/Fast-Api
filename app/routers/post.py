from fastapi import HTTPException, status, Response, Depends, APIRouter
from typing import List
from sqlalchemy.orm import Session
from .. import schemas, models, oauth2
from .. database import get_db

router = APIRouter(
    prefix= "/posts",
    tags=['Posts']
)

my_post = [{"title":"favorite food", "content":"I like Pizza", "id":2}]

@router.get("/", response_model=List[schemas.PostResponse])
def get_posts(db:Session = Depends(get_db), user_id : int = Depends(oauth2.get_current_user)):
    posts = db.query(models.Post).filter(models.Post.user_id == user_id.id).all()
    return posts

@router.post("/", status_code= status.HTTP_201_CREATED, response_model=schemas.PostResponse)
def create_post(post:schemas.CreatePost, db:Session = Depends(get_db), user_id : int = Depends(oauth2.get_current_user)):
   new_post = models.Post(user_id = user_id.id, **post.dict())
   db.add(new_post)
   db.commit()
   db.refresh(new_post)
   print(user_id)
   return new_post

def find_post(id):
    for p in my_post:
        if p['id'] == id:
            return p

@router.get("/{id}", response_model= schemas.PostResponse, ) 
def get_post(id:int, response:Response, db:Session = Depends(get_db), user_id : int = Depends(oauth2.get_current_user)):
   post = db.query(models.Post).filter(models.Post.id == id).first()

   if not post:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= f"post with {id} not found"
        )
   return post



@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int, db:Session = Depends(get_db), user_id : int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)

    post = post_query.first()

    if post == None:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= f"post with {id} doesnt exist"
        )

    if post.user_id != user_id.id:
        raise HTTPException(
            status_code= status.HTTP_403_FORBIDDEN,
            detail="Not Authorised for requested Action"
        )
    
    post_query.delete(synchronize_session= False)
    db.commit()
    return Response(status_code= status.HTTP_204_NO_CONTENT)

@router.put("/{id}")
def update_post(id:int, updated_post:schemas.CreatePost, db:Session = Depends(get_db), user_id : int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    

    if post is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"post with {id} doesnt exist"
        )

    if post.user_id != user_id.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not Authorised For Requested Action"
        )

    post_query.update(updated_post.dict(), synchronize_session= False)
    db.commit()

    return post_query.first() 
