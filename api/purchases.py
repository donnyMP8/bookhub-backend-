from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from db.models import Purchase, User, Book
from schemas.purchases import PurchaseCreate, PurchaseRead

router = APIRouter(prefix="/purchases", tags=["Purchases"])


@router.post("/", response_model=PurchaseRead)
def create_purchase(data: PurchaseCreate, db: Session = Depends(get_db)):
    user = db.query(User).get(data.user_id)
    book = db.query(Book).get(data.book_id)

    if not user or not book:
        raise HTTPException(404, "User or Book not found")

    purchase = Purchase(**data.dict())
    db.add(purchase)
    db.commit()
    db.refresh(purchase)

    return purchase


@router.get("/", response_model=list[PurchaseRead])
def list_purchases(db: Session = Depends(get_db)):
    return db.query(Purchase).all()
