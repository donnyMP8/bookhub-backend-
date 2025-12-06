from typing import List
import time
import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input("\nPress Enter to continue...")


def menu_title(title: str):
    clear()
    print("=" * 40)
    print(title.upper())
    print("=" * 40)


# --------- FIXED TYPING HERE ---------
# OLD (FAILED in Python 3.8):
# def choose(prompt_text: str, choices: list[str]):

def choose(prompt_text: str, choices: List[str]):
# -------------------------------------

    print(prompt_text)
    for index, choice in enumerate(choices, start=1):
        print(f"{index}. {choice}")

    while True:
        try:
            selection = int(input("Choose an option: "))
            if 1 <= selection <= len(choices):
                return choices[selection - 1]
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Enter a valid number.")
