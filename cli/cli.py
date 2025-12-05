import typer
from rich import print
#from backend.db.database import Base, engine
#from backend.db.seed import seed_data
from .menu_users import users_menu
from .menu_books import books_menu
from .menu_borrows import borrows_menu
from .menu_purchases import purchases_menu
from .helpers import menu_title, choose
from db.database import Base, engine
from db.seed import seed_data

app = typer.Typer()

@app.command()
def create_tables():
    Base.metadata.create_all(bind=engine)
    print("[green]Tables created![/green]")

@app.command()
def seed():
    seed_data()

@app.command()
def menu():
    while True:
        menu_title("📚 Library Management System")

        choice = choose("Choose", ["1","2","3","4","5","0"])

        if choice == "1":
            users_menu()
        elif choice == "2":
            books_menu()
        elif choice == "3":
            purchases_menu()
        elif choice == "4":
            borrows_menu()
        elif choice == "5":
            seed_data()
        elif choice == "0":
            print("[cyan]Goodbye![/cyan]")
            break

if __name__ == "__main__":
    app()
