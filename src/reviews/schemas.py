from pydantic import BaseModel
import sqlalchemy.dialects.postgresql as pg
from sqlmodel import Field, Column
import uuid
from typing import Optional
from datetime import datetime


class ReviewModel(BaseModel):
    uid: uuid.UUID 
    rating : int = Field(le=5)
    review_text : str
    user_uid : Optional[uuid.UUID]
    book_uid : Optional[uuid.UUID] 
    created_at : datetime 
    update_at : datetime

class ReviewCreateModel(BaseModel):
    rating : int = Field(le=5)
    review_text : str