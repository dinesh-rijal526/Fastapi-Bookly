from pydantic import BaseModel
import uuid
from datetime import datetime, date
from typing import List
from src.reviews.schemas import ReviewModel

class Books(BaseModel):
    uid: uuid.UUID
    title : str
    author : str
    publisher : str
    published_date : date
    page : int
    language : str
    created_at : datetime
    update_at : datetime

class BookDetailModel(Books):
    reviews : List[ReviewModel] 

class BookCreateMOdel(BaseModel):
    title : str
    author : str
    publisher : str
    published_date : date
    page : int
    language : str

class BookUpdateModel(BaseModel):
    title : str
    author : str
    publisher : str
    page : int
    language : str