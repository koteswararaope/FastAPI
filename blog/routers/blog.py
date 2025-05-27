from fastapi import APIRouter, Depends,status, Response,Request, HTTPException
from .. import schemas, database
from sqlalchemy.orm import Session
from .. import models
from typing import List

from .oauth2 import get_current_user
router =APIRouter(
    tags=["Blogs"]
)

get_db = database.get_db
@router.get('/blog', response_model=List[schemas.ShowBlog] )
def get_allblogs(db:Session = Depends(get_db),get_current_user: schemas.User= Depends(get_current_user)):
    blogs= db.query(models.Blog).all()
    return blogs

@router.post('/',status_code=status.HTTP_201_CREATED )
def create_blog(blog:schemas.Blog, db:Session = Depends(get_db),get_current_user: schemas.User= Depends(get_current_user)):
    new_blog= models.Blog(title = blog.title, body=blog.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.get('/blog/{id}',status_code=status.HTTP_200_OK,response_model=schemas.ShowBlog )
def get_blog_id(id,response :Response,db:Session = Depends(get_db),get_current_user: schemas.User= Depends(get_current_user)):
    blog= db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
       # response.status_code= status.HTTP_404_NOT_FOUND
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the id {id} not found in db")
    return blog

@router.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT )
def deleteblogbyid(id,response:Response, db:Session = Depends(get_db),get_current_user: schemas.User= Depends(get_current_user)):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return status.HTTP_200_OK

@router.put('/blog/{id}', status_code=status.HTTP_200_OK )
def Deletebyid(id, request:schemas.Blog, db:Session = Depends(database.get_db),get_current_user: schemas.User= Depends(get_current_user)):
     blog = db.query(models.Blog).filter(models.Blog.id == id)
     if not blog.first():
         raise HTTPException(status.HTTP_404_NOT_FOUND)
     else:
         blog.update({"title":request.title,"body":request.body})
         db.commit()
     return f"db with id {id} is updated"