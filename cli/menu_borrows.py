from rich import print
from sqlalchemy.orm import Session
from backend.db.database import SessionLocal
from backend.db.models import Borrow
from .helpers import menu_title, choose, pause

def list_borrows():
    db = SessionLocal()
    menu_title("All Borrows")

    for b in db.query(Borrow).all():
        print(f"[green]{b.id}[/green] - User {b.user_id} borrowed Book {b.book_id} (returned={b.returned})")

    pause()

def borrows_menu():
    while True:
        menu_title("Borrows Menu")
        choice = choose("Choose", ["1","0"])

        if choice == "1":
            list_borrows()
        elif choice == "0":
            break
