from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import User, Book, Purchase, Borrow
from datetime import datetime

def seed_data():
    db: Session = SessionLocal()

    print(" Seeding database...")

    # Clear old data (optional, remove if not needed)
    db.query(Purchase).delete()
    db.query(Borrow).delete()
    db.query(Book).delete()
    db.query(User).delete()
    db.commit()

    # --- Users ---
    user1 = User(name="Alice", email="alice@example.com")
    user2 = User(name="Bob", email="bob@example.com")

    db.add_all([user1, user2])
    db.commit()

    # --- Books ---
    book1 = Book(title="The Pragmatic Programmer", author="Andrew Hunt", price=39.99, stock=10)
    book2 = Book(title="Clean Code", author="Robert C. Martin", price=29.99, stock=5)
    book3 = Book(title="Deep Learning", author="Ian Goodfellow", price=59.99, stock=3)

    db.add_all([book1, book2, book3])
    db.commit()

    # --- Purchases ---
    purchase1 = Purchase(user_id=user1.id, book_id=book1.id)
    purchase2 = Purchase(user_id=user2.id, book_id=book3.id)

    db.add_all([purchase1, purchase2])
    db.commit()

    # --- Borrows ---
    borrow1 = Borrow(user_id=user1.id, book_id=book2.id, returned=False)
    borrow2 = Borrow(user_id=user2.id, book_id=book1.id, returned=True, borrowed_at=datetime(2024, 1, 10))

    db.add_all([borrow1, borrow2])
    db.commit()

    print("✅ Database seeded successfully!")

if __name__ == "__main__":
    seed_data()
