from pydantic import BaseModel, Field
import uuid
from datetime import datetime

class UserCreateModel(BaseModel):
    first_name : str = Field(max_length=20)
    last_name :str = Field(max_length=20)
    username : str = Field(max_length=12)
    email : str = Field(max_length=50)
    password : str = Field(min_length=6)

class UserModel(BaseModel):
    uid : uuid.UUID
    username : str
    email : str
    first_name :str
    last_name : str
    is_verified : bool
    password_hash : str = Field(exclude=True)
    created_at : datetime 
    update_at : datetime 