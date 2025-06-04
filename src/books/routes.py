from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException
from typing import List
from .service import BookService
from src.books.schemas import Books, BookUpdateModel, BookCreateMOdel
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session


book_router = APIRouter()
book_service = BookService()


@book_router.get('/', response_model=List[Books])
async def get_all_books(session:AsyncSession = Depends(get_session)) :
    books =await book_service.get_all_books(session)
    return books

@book_router.post('/', status_code=status.HTTP_201_CREATED, response_model=Books)
async def create_a_book(book_data:BookCreateMOdel, session:AsyncSession = Depends(get_session)) :
    new_book =await book_service.create_book(book_data, session)
    return new_book

@book_router.get('/{book_uid}', response_model=Books)
async def get_book(book_uid:str, session:AsyncSession = Depends(get_session)) :
    book =await book_service.get_book(book_uid, session)
    if book is  None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book not found")
    else:    
        return book


@book_router.patch('/{book_uid}', response_model=Books)
async def update_book(book_uid:str, book_update_data:BookUpdateModel, session:AsyncSession = Depends(get_session)) :
    updated_book =await book_service.update_book(book_uid,book_update_data, session)
    if updated_book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book not found")
    else:
        return updated_book



@book_router.delete('/{book_uid}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_uid:str, session:AsyncSession = Depends(get_session)) :
    book_to_delete = await book_service.delete_book(book_uid, session)
    if book_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book not found")
    else:
        return {}
   