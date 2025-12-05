from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from db.models import Borrow, User, Book
from schemas.borrows import BorrowCreate, BorrowRead

router = APIRouter(prefix="/borrows", tags=["Borrows"])


@router.post("/", response_model=BorrowRead)
def borrow_book(data: BorrowCreate, db: Session = Depends(get_db)):
    user = db.query(User).get(data.user_id)
    book = db.query(Book).get(data.book_id)

    if not user or not book:
        raise HTTPException(404, "User or Book not found")

    borrow = Borrow(**data.dict())
    db.add(borrow)
    db.commit()
    db.refresh(borrow)

    return borrow


@router.put("/{borrow_id}/return", response_model=BorrowRead)
def return_book(borrow_id: int, db: Session = Depends(get_db)):
    borrow = db.query(Borrow).get(borrow_id)
    if not borrow:
        raise HTTPException(404, "Borrow record not found")

    borrow.returned = True
    db.commit()
    db.refresh(borrow)
    return borrow


@router.get("/", response_model=list[BorrowRead])
def list_borrows(db: Session = Depends(get_db)):
    return db.query(Borrow).all()
