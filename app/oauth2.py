from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional
from sqlalchemy.orm import Session
from . import schemas, database, models
from .database import get_db
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


SECRET_KEY = "hello"
ALGORITHM = "HS256"
ACESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data:dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes= ACESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp" : expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm= ALGORITHM)

    return encoded_jwt

def verify_access_token(token:str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id:Optional[str] = payload.get("user_id")

        if id is None:
            raise credentials_exception

        token_data = schemas.TokenData(id = str(id))

    except JWTError:
        raise credentials_exception

    return token_data

def current_user(token:str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code= status.HTTP_401_UNAUTHORIZED,
        detail= f"could not validate credentials",
        headers= {"www-Authenticate":"Bearer"})

    return verify_access_token(token, credentials_exception)

def get_current_user(token: str = Depends(oauth2_scheme), db:Session = Depends(database.get_db)):
    credentials_exception = HTTPException(
        status_code= status.HTTP_401_UNAUTHORIZED,
        detail= "could not validate credentials",
        headers= {"www-Authenticate" : "Bearer"}
    )

    token_data = verify_access_token(token, credentials_exception)
    user = db.query(models.user).filter(
        models.user.id == int(token_data.id)
    ).first()

    return user
