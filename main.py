from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
app = FastAPI()

@app.get('/')
def index():
    return {'data':{'name':"Megha"}}

@app.get('/blog')
def Blog(limit=10, published: bool =True, sort: Optional[str]=None ):
    if published == True:
        return {'data':f'{limit} published blogs from db'} 
    else:
        return {'data':f'{limit} un-published blogs from db'} 

@app.get('/about')
def about():
    return{"about page"}

@app.get('/blog/unpublished')
def unplublished():
    return {'data':'Unpublished blobs'}

'''@app.get('/blog/{id}')
def show(id:int):
    return {'data':id}''' #detch blg with id

@app.get('/blog/{id}/comments')
def Comments(id):
    return {'data':{'1','2'}} #fecth comments for blog for id

class Blog(BaseModel):
    title: str
    body : str
    published_at :Optional[bool]
    
@app.post('/blog')
def create_blog(blog:Blog): 
    return{'data':f'Blog is created with title {blog.title}'}