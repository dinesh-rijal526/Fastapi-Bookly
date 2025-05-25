from pydantic import BaseModel


class Books(BaseModel):
    id: int
    title : str
    author : str
    publisher : str
    published_date : str
    page : int
    language : str

class BookUpdateModel(BaseModel):
    title : str
    author : str
    publisher : str
    published_date : str
    page : int
    language : str