from rich import print
from db.database import SessionLocal
from db.models import Book
from cli.helpers import menu_title, choose, pause

def list_books():
    db = SessionLocal()
    menu_title("All Books")

    for b in db.query(Book).all():
        print(f"[green]{b.id}[/green] - {b.title} by {b.author} / ${b.price} / stock: {b.stock}")

    db.close()
    pause()

def add_book():
    db = SessionLocal()
    menu_title("Add Book")

    title = input("Title: ")
    author = input("Author: ")
    price = float(input("Price: "))
    stock = int(input("Stock: "))

    book = Book(title=title, author=author, price=price, stock=stock)
    db.add(book)
    db.commit()

    print("[green]✅ Book added![/green]")
    db.close()
    pause()

def update_stock():
    db = SessionLocal()
    menu_title("Update Stock")

    book_id = int(input("Book ID: "))
    amount = int(input("New stock: "))

    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        print("[red]❌ Book not found[/red]")
    else:
        book.stock = amount
        db.commit()
        print("[green]✅ Stock updated![/green]")

    db.close()
    pause()

def delete_book():
    db = SessionLocal()
    menu_title("Delete Book")

    book_id = int(input("Book ID: "))
    book = db.query(Book).filter(Book.id == book_id).first()

    if not book:
        print("[red]❌ Book not found[/red]")
    else:
        db.delete(book)
        db.commit()
        print("[green]✅ Book deleted[/green]")

    db.close()
    pause()

def books_menu():
    while True:
        menu_title("📚 Books Menu")
        print("1. List Books")
        print("2. Add Book")
        print("3. Update Stock")
        print("4. Delete Book")
        print("0. Back")
        
        choice = choose("Choose", ["1","2","3","4","0"])

        if choice == "1":
            list_books()
        elif choice == "2":
            add_book()
        elif choice == "3":
            update_stock()
        elif choice == "4":
            delete_book()
        elif choice == "0":
            break