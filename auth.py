import os
import hashlib
from getpass import getpass
from rich.console import Console

console = Console()


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def login():
    if not os.path.exists("master.key"):
        master = getpass("Create Master Password: ")
        hash_password(master)
        hashed = hash_password(master)
        with open("master.key", "w") as file:
            file.write(hashed)

    with open("master.key") as file:
        saved_hash = file.read()
        master = getpass("Master Password: ")
        if hash_password(master) == saved_hash:
            console.print("[bold blue]Welcome")
            return True
        else:
            console.print("[bold red]wrong Password")
            return False
