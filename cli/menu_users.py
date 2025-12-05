from rich import print
from sqlalchemy.orm import Session
from backend.db.database import SessionLocal
from backend.db.models import User
from .helpers import menu_title, choose, pause

def list_users():
    db: Session = SessionLocal()
    menu_title("All Users")

    users = db.query(User).all()
    for u in users:
        print(f"[green]{u.id}[/green] - {u.name} ({u.email})")

    pause()

def create_user():
    db: Session = SessionLocal()
    menu_title("Create User")

    name = input("Name: ")
    email = input("Email: ")

    user = User(name=name, email=email)
    db.add(user)
    db.commit()

    print("[bold green]User created![/bold green]")
    pause()

def delete_user():
    db: Session = SessionLocal()
    menu_title("Delete User")

    user_id = int(input("User ID: "))
    user = db.query(User).filter_by(id=user_id).first()

    if not user:
        print("[red]User not found[/red]")
    else:
        db.delete(user)
        db.commit()
        print("[green]Deleted successfully.[/green]")

    pause()

def users_menu():
    while True:
        menu_title("Users Menu")
        choice = choose(
            "Select an option",
            ["1","2","3","0"]
        )

        if choice == "1":
            list_users()
        elif choice == "2":
            create_user()
        elif choice == "3":
            delete_user()
        elif choice == "0":
            break
