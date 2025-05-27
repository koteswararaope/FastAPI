from fastapi import APIRouter, Depends,status, Response,Request, HTTPException
from .. import database, schemas, models
from sqlalchemy.orm import Session
from ..hashing import Hash

router= APIRouter(
    tags=["Users"]
)

get_db= database.get_db
@router.post('/user',response_model=schemas.Showuser )
def create_user(request:schemas.User,db:Session = Depends(get_db)):
    hassed_pwd= Hash.encrypt(request.password)
    new_user = models.User(name=request.name,email=request.email,password=hassed_pwd)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/user/{id}',response_model=schemas.Showuser )
def getuserbyid(id, db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id ==id).first()
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    return user