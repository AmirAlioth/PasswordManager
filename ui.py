from pyfiglet import Figlet
from rich.panel import Panel
from rich.console import Console
from rich.table import Table
from database import data, search, copy_password
from encryption import encrypt, decrypt
import string
import secrets
import random
import pyperclip

console = Console()


def logo():
    smslant_font = Figlet(font="smslant")
    console.print(smslant_font.renderText("Password"))


def menu_panel():
    console.print(
        Panel(
            "[bold cyan]1- Add Password\n2- Show Password\n3- Search password\n4- Generate Password\n5- [bold green]Update [bold cyan]Password\n6- [bold red]Delete [bold cyan]password[bold red]\n7- Exit",
            title="menu"
        )
    )


def get_data():
    console.print("[bold blue]Website: ")
    website = input()
    console.print("[bold blue]Username: ")
    username = input()
    console.print("[bold blue]Password: ")
    password = input()
    encrypt_password = encrypt(password)

    return website, username, encrypt_password


def show_data():
    table = Table(title="passwords")
    table.add_column("ID", style="red", justify="center")
    table.add_column("website", style="blue")
    table.add_column("username", style="green")
    table.add_column("password", style="yellow")

    passwords = data()

    for password in passwords:
        table.add_row(
            str(password[0]),
            password[1],
            password[2],
            decrypt(password[3])
        )
    console.print(table)


def copy_pass():
    console.print("[bold blue]id for copy password: ")
    copy_id = input()
    real_password = copy_password(copy_id)
    if real_password is None:
        console.print("[bold red]id not find!")
    else:
        pyperclip.copy(decrypt("".join(real_password)))
        console.print("[bold green]Password copied to clipboard!")


def show_search(results):
    table = Table(title="we find")
    table.add_column("ID", style="red", justify="center")
    table.add_column("website", style="blue")
    table.add_column("username", style="green")
    table.add_column("password", style="yellow")

    for result in results:
        table.add_row(
            str(result[0]),
            (result[1]),
            (result[2]),
            decrypt(result[3])
        )
    console.print(table)


def generate_password(length):

    lowercase_characters = string.ascii_lowercase
    lowercase_key = (secrets.choice(lowercase_characters))
    uppercase_characters = string.ascii_uppercase
    uppercase_key = (secrets.choice(uppercase_characters))
    digits_characters = string.digits
    digits_key = (secrets.choice(digits_characters))
    symbols_characters = string.punctuation
    symbols_key = (secrets.choice(symbols_characters))

    keys = [
        lowercase_key,
        uppercase_key,
        digits_key,
        symbols_key
    ]

    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(characters) for i in range(length - 4))
    for i in password:
        keys.append(i)

    random.shuffle(keys)

    return "".join(keys)
