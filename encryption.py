from cryptography.fernet import Fernet


def load_key():
    with open("secret.key", "rb") as file:
        return file.read()


key = load_key()
f = Fernet(key)


def encrypt(text):
    encrypted = f.encrypt(text.encode())
    return encrypted.decode()


def decrypt(text):
    decrypt = f.decrypt(text.encode())
    return decrypt.decode()
