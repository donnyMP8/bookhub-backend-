from sqlalchemy.orm import Session
from sqlalchemy import or_
from typing import Optional  # Added
from db.models import Book

def search_books(
    db: Session, 
    query: Optional[str] = None,  # Changed from = None (implicit)
    min_price: Optional[float] = None,  # Changed
    max_price: Optional[float] = None  # Changed
):
    q = db.query(Book)

    if query:
        q = q.filter(
            or_(
                Book.title.ilike(f"%{query}%"),
                Book.author.ilike(f"%{query}%")
            )
        )

    if min_price is not None:
        q = q.filter(Book.price >= min_price)

    if max_price is not None:
        q = q.filter(Book.price <= max_price)

    return q.all()