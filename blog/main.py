from fastapi import FastAPI, Depends, status, Response, HTTPException
from pydantic import BaseModel
from . import schemas
from .import models
from . import database
from .database import engine,sessinlocal
from sqlalchemy.orm import Session
from typing import List
from .hashing import Hash
from .routers import blog,user,authentication

app = FastAPI()

models.Base.metadata.create_all(engine)
app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
        
'''@app.post('/',status_code=status.HTTP_201_CREATED,tags=["Blog"])
def crate_blog(blog:schemas.Blog, db:Session = Depends(database.get_db)):
    new_blog= models.Blog(title = blog.title, body=blog.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog'''

'''@app.get('/blog', response_model=List[schemas.ShowBlog],tags=["Blog"])
def get_allblogs(db:Session = Depends(get_db)):
    blogs= db.query(models.Blog).all()
    return blogs'''

'''@app.get('/blog/{id}',status_code=status.HTTP_200_OK,response_model=schemas.ShowBlog,tags=["Blog"])
def get_blog_id(id,response :Response,db:Session = Depends(database.get_db)):
    blog= db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
       # response.status_code= status.HTTP_404_NOT_FOUND
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the id {id} not found in db")
    return blog'''

'''@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT,tags=["Blog"])
def deleteblogbyid(id,response:Response, db:Session = Depends(database.get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return status.HTTP_200_OK'''
    
'''@app.put('/blog/{id}', status_code=status.HTTP_200_OK,tags=["Blog"])
def Deletebyid(id, request:schemas.Blog, db:Session = Depends(database.get_db)):
     blog = db.query(models.Blog).filter(models.Blog.id == id)
     if not blog.first():
         raise HTTPException(status.HTTP_404_NOT_FOUND)
     else:
         blog.update({"title":request.title,"body":request.body})
         db.commit()
     return f"db with id {id} is updated"'''
 


'''@app.post('/user',response_model=schemas.Showuser,tags=["User"])
def create_user(request:schemas.User,db:Session = Depends(database.get_db)):
    hassed_pwd= Hash.encrypt(request.password)
    new_user = models.User(name=request.name,email=request.email,password=hassed_pwd)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get('/user/{id}',response_model=schemas.Showuser,tags=["User"])
def getuserbyid(id, db:Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id ==id).first()
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    return user'''