from fastapi import HTTPException, status, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, utils
from .. database import get_db

router = APIRouter(
    prefix= "/users",
    tags=['User']
)

@router.post("/", status_code= status.HTTP_201_CREATED, response_model= schemas.Userout)
def create_user(user:schemas.Usercreate, db:Session = Depends(get_db)):
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_user = models.user(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.get("/{id}", response_model= schemas.Userout)
def get_user(id:int, db:Session = Depends(get_db)):
    user = db.query(models.user).filter(models.user.id == id).first()

    if not user:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail = f"user with {id} doesnot exist"
        )
    return user