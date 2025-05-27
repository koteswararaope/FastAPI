from pydantic import BaseModel

class Blog(BaseModel):
    title:str
    body:str
    
class ShowBlog(BaseModel):
    title:str
    body:str

class User(BaseModel):
    name:str
    password:str
    email:str
class Showuser(BaseModel):
    name:str
    email:str
class Login(BaseModel):
    username:str
    password:str
    
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str | None = None