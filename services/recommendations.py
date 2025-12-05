from sqlalchemy.orm import Session
from sqlalchemy import func
from db.models import Book, Purchase, Borrow


def get_user_recommendations(db: Session, user_id: int):
    """
    Recommend books based on user history:
    - purchase history
    - borrow history
    - authors they like
    - fallback to popular books
    """

    # 1️⃣ Books the user interacted with
    user_purchases = db.query(Purchase.book_id).filter(Purchase.user_id == user_id)
    user_borrows = db.query(Borrow.book_id).filter(Borrow.user_id == user_id)

    user_book_ids = {b.book_id for b in user_purchases.union(user_borrows)}

    # 2️⃣ Favorite authors
    favorite_authors = (
        db.query(Book.author)
        .filter(Book.id.in_(user_book_ids))
        .distinct()
        .all()
    )

    favorite_authors = [a[0] for a in favorite_authors if a[0]]

    # 3️⃣ Recommend books by similar authors
    recs = (
        db.query(Book)
        .filter(Book.author.in_(favorite_authors))
        .filter(~Book.id.in_(user_book_ids))
        .all()
    )

    if recs:
        return recs

    # 4️⃣ Fallback → top selling books
    top_sales = (
        db.query(Book)
        .join(Purchase)
        .group_by(Book.id)
        .order_by(func.count(Purchase.id).desc())
        .limit(5)
        .all()
    )

    if top_sales:
        return top_sales

    # 5️⃣ Final fallback → most borrowed books
    top_borrows = (
        db.query(Book)
        .join(Borrow)
        .group_by(Book.id)
        .order_by(func.count(Borrow.id).desc())
        .limit(5)
        .all()
    )

    return top_borrows
