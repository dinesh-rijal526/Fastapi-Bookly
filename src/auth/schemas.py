from pydantic import BaseModel, Field
import uuid
from datetime import datetime
from typing import List
from src.db.models import Book
from src.reviews.schemas import ReviewModel

class UserCreateModel(BaseModel):
    first_name : str = Field(max_length=20)
    last_name :str = Field(max_length=20)
    username : str = Field(max_length=12)
    email : str = Field(max_length=50)
    password : str = Field(min_length=6)
    role : str

class UserModel(BaseModel):
    uid : uuid.UUID
    username : str
    email : str
    first_name :str
    last_name : str
    is_verified : bool
    password_hash : str = Field(exclude=True)
    role : str 
    created_at : datetime 
    update_at : datetime 

class UserBooksModel(UserModel):
    books : List[Book]
    reviews : List[ReviewModel]

class UserLoginModel(BaseModel):
    email : str = Field(max_length=50)
    password : str = Field(min_length=6)