from rich import print
from db.database import SessionLocal
from db.models import Purchase
from cli.helpers import menu_title, choose, pause

def list_purchases():
    db = SessionLocal()
    menu_title("All Purchases")

    for p in db.query(Purchase).all():
        print(f"[green]{p.id}[/green] - User {p.user_id} bought Book {p.book_id} on {p.date}")

    db.close()
    pause()

def purchases_menu():
    while True:
        menu_title("💰 Purchases Menu")
        print("1. List Purchases")
        print("0. Back")
        
        choice = choose("Choose", ["1","0"])

        if choice == "1":
            list_purchases()
        elif choice == "0":
            break