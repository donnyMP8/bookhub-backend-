from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List  # Added
from db.database import get_db
from db.models import Purchase, User, Book
from schemas.purchases import PurchaseCreate, PurchaseRead

router = APIRouter(prefix="/purchases", tags=["Purchases"])


@router.post("/", response_model=PurchaseRead)
def create_purchase(data: PurchaseCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == data.user_id).first()
    book = db.query(Book).filter(Book.id == data.book_id).first()

    if not user or not book:
        raise HTTPException(404, "User or Book not found")

    purchase = Purchase(**data.dict())
    db.add(purchase)
    db.commit()
    db.refresh(purchase)

    return purchase


@router.get("/", response_model=List[PurchaseRead])  # Changed from list[PurchaseRead]
def list_purchases(db: Session = Depends(get_db)):
    return db.query(Purchase).all()