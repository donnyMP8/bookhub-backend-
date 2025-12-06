from rich import print
from db.database import SessionLocal
from db.models import Borrow
from cli.helpers import menu_title, choose, pause

def list_borrows():
    db = SessionLocal()
    menu_title("All Borrows")

    for b in db.query(Borrow).all():
        status = "✅ Returned" if b.returned else "📖 Active"
        print(f"[green]{b.id}[/green] - User {b.user_id} borrowed Book {b.book_id} ({status})")

    db.close()
    pause()

def borrows_menu():
    while True:
        menu_title("📖 Borrows Menu")
        print("1. List Borrows")
        print("0. Back")
        
        choice = choose("Choose", ["1","0"])

        if choice == "1":
            list_borrows()
        elif choice == "0":
            break