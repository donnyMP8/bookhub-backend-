from rich.console import Console
from rich.prompt import Prompt

console = Console()

def menu_title(title: str):
    console.print(f"\n[bold cyan]=== {title} ===[/bold cyan]\n")

def pause():
    input("\nPress ENTER to continue...")

def choose(prompt_text: str, choices: list[str]):
    choice = Prompt.ask(prompt_text, choices=choices)
    return choice
