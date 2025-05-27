from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from .. import schemas
from .. import database,models,hashing
from .. hashing import Hash
from datetime import datetime, timedelta, timezone
from .token import create_access_token
from fastapi.security import OAuth2PasswordRequestForm
ACCESS_TOKEN_EXPIRE_MINUTES = 30
router= APIRouter(tags=["Authentication"])
get_db = database.get_db

@router.post('/login')
def login(request:OAuth2PasswordRequestForm =Depends(),  db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND,detail="Invalid credentials")
    if not Hash.verify(user.password,request.password):
        raise HTTPException(status.HTTP_404_NOT_FOUND,detail="Invalid credentials")
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}
    )
    return {"access_token":access_token, "token_type" :"bearer"}
    

'''user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND,detail="Invalid credentials")'''