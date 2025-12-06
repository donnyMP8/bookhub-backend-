import typer
from rich import print
from cli.menu_users import users_menu
from cli.menu_books import books_menu
from cli.menu_borrows import borrows_menu
from cli.menu_purchases import purchases_menu
from cli.helpers import menu_title, choose
from db.database import Base, engine
from db.seed import seed_data

app = typer.Typer()

@app.command()
def create_tables():
    """Create all database tables"""
    Base.metadata.create_all(bind=engine)
    print("[green]✅ Tables created![/green]")

@app.command()
def seed():
    """Seed the database with sample data"""
    seed_data()

@app.command()
def menu():
    """Launch the interactive CLI menu"""
    while True:
        menu_title("📚 Library Management System")
        print("1. Users")
        print("2. Books")
        print("3. Purchases")
        print("4. Borrows")
        print("5. Seed Database")
        print("0. Exit")

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
            print("[cyan]👋 Goodbye![/cyan]")
            break

if __name__ == "__main__":
    app()