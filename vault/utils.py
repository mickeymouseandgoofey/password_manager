import os
from decouple import config
from cryptography.fernet import Fernet

# Load and validate the encryption key
fernet_key = config("FERNET_KEY")
if not fernet_key:
    raise ValueError("FERNET_KEY is not set in the environment.")

fernet = Fernet(fernet_key.encode())

def encrypt_password(password: str) -> str:
    """Encrypts a plaintext password."""
    return fernet.encrypt(password.encode()).decode()

def decrypt_password(encrypted_password: str) -> str:
    """Decrypts an encrypted password token."""
    return fernet.decrypt(encrypted_password.encode()).decode()
