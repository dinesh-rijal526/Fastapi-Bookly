from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.models import User
from .service import ReviewService
from .schemas import ReviewCreateModel
from src.db.main import get_session
from src.auth.dependencies import current_user

review_router = APIRouter()
review_service = ReviewService()

@review_router.post('/book/{book_uid}')
async def add_review_to_book(
    book_uid : str,
    review_data : ReviewCreateModel,
    current_user : User = Depends(current_user),
    session : AsyncSession = Depends(get_session)
):
    new_review = await review_service.add_review_to_book(
        user_email=current_user.email,
        book_uid=book_uid,
        review_data=review_data,
        session=session
    )

    return new_review

@review_router.get('/book')
async def get_revier_book(
    review_data : ReviewCreateModel,
    current_user : User = Depends(current_user),
    session : AsyncSession = Depends(get_session)
):
    pass