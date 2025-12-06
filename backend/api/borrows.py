from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List  # Added
from db.database import get_db
from db.models import Borrow, User, Book
from schemas.borrows import BorrowCreate, BorrowRead

router = APIRouter(prefix="/borrows", tags=["Borrows"])


@router.post("/", response_model=BorrowRead)
def borrow_book(data: BorrowCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == data.user_id).first()
    book = db.query(Book).filter(Book.id == data.book_id).first()

    if not user or not book:
        raise HTTPException(404, "User or Book not found")

    borrow = Borrow(**data.dict())
    db.add(borrow)
    db.commit()
    db.refresh(borrow)

    return borrow


@router.put("/{borrow_id}/return", response_model=BorrowRead)
def return_book(borrow_id: int, db: Session = Depends(get_db)):
    borrow = db.query(Borrow).filter(Borrow.id == borrow_id).first()
    if not borrow:
        raise HTTPException(404, "Borrow record not found")

    borrow.returned = True
    db.commit()
    db.refresh(borrow)
    return borrow


@router.get("/", response_model=List[BorrowRead])  # Changed from list[BorrowRead]
def list_borrows(db: Session = Depends(get_db)):
    return db.query(Borrow).all()