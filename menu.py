from ui import logo, get_data, menu_panel, show_data, show_search, generate_password, copy_pass
from database import save_data, search, delete_password, update_password
from rich.console import Console
from auth import login
from encryption import encrypt
import pyperclip

console = Console()


def menu():
    logo()
    if not login():
        return
    while True:
        menu_panel()
        choice = input()

        if choice == "1":

            results = get_data()

            if results is not None:
                website, username, password = results
                save_data(website, username, password)

        elif choice == "2":
            show_data()
            console.print("[bold blue]Press 1 if you want copy password")
            choice_copy = input()
            if choice_copy == "1":
                copy_pass()
            else:
                continue

        elif choice == "3":
            keyword = input("Search website: ")

            results = search(keyword)

            show_search(results)

        elif choice == "4":
            console.print("[bold blue]length:")
            key_lengh = int(input())
            if key_lengh <= 4:
                console.print(
                    "[bold red]Password lengh have to be biger than 4")

            else:
                strong_pass = generate_password(key_lengh)
                console.print(strong_pass)
                console.print("[bold blue]Press 1 for copy password: ")
                copy_choice = input()
                if copy_choice == "1":
                    pyperclip.copy(strong_pass)
                else:
                    continue

        elif choice == "5":
            show_data()
            console.print("[blue]id: ")
            update_id = input()
            console.print("[blue]New Website: ")
            update_website = input()
            console.print("[blue]New Username: ")
            update_username = input()
            console.print("[blue]New Password: ")
            update_Pass = input()
            encrypt_pass = encrypt(update_Pass)

            update_password(update_id, update_website,
                            update_username, encrypt_pass)
            show_data()

        elif choice == "6":
            show_data()
            console.print("[bold red]Password id for delete: ")
            delete_id = input()
            delete_password(delete_id)

        elif choice == "7":
            break
