from fastapi import FastAPI
from src.books.routes import book_router
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from src.db.main import init_db

@asynccontextmanager
async def life_span(app:FastAPI):
    print(f"Server is Starting...")
    await init_db()
    yield
    print(f"Server has been Stopped..")

version = 'v1'

app = FastAPI(
    title= 'Bookly',
    description= 'A REST API Service for book review',
    version= version,
    lifespan=life_span
)
app.add_middleware(CORSMiddleware, allow_origins=["*"],allow_methods=["*"], allow_headers=["*"])

app.include_router(book_router, prefix=f'/api/{version}/books', tags=['books'])