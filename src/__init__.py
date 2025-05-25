from fastapi import FastAPI
from src.books.routes import book_router
from fastapi.middleware.cors import CORSMiddleware

version = 'v1'

app = FastAPI(
    title= 'Bookly',
    description= 'A REST API Service for book review',
    version= version
)
app.add_middleware(CORSMiddleware, allow_origins=["*"],allow_methods=["*"], allow_headers=["*"])

app.include_router(book_router, prefix=f'/api/{version}/books', tags=['books'])