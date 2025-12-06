from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional  # Added
from db.database import get_db
from db.models import Book
from schemas.books import BookCreate, BookRead
from services.search import search_books

router = APIRouter(prefix="/books", tags=["Books"])


@router.post("/", response_model=BookRead)
def create_book(data: BookCreate, db: Session = Depends(get_db)):
    book = Book(**data.dict())
    db.add(book)
    db.commit()
    db.refresh(book)
    return book


@router.get("/", response_model=List[BookRead])  # Changed from list[BookRead]
def list_books(db: Session = Depends(get_db)):
    return db.query(Book).all()


@router.get("/{book_id}", response_model=BookRead)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(404, "Book not found")
    return book


@router.get("/search/", response_model=List[BookRead])  # Changed from list[BookRead]
def search(
    q: str = "",
    min_price: Optional[float] = None,  # Changed from float | None
    max_price: Optional[float] = None,  # Changed from float | None
    db: Session = Depends(get_db),
):
    return search_books(db, q, min_price, max_price)