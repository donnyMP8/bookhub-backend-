from sqlalchemy.orm import Session
from sqlalchemy import or_
from db.models import Book

def search_books(db: Session, query: str = None, min_price: float = None, max_price: float = None):
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
