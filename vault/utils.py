from cryptography.fernet import Fernet
import os

key = os.environ.get('FERNET_KEY')
f = Fernet(key)

def encrypt_password(password):
    return f.encrypt(password.encode()).decode()


def decrypt_password(token):
    return f.decrypt(token.encode()).decode()
 

def decrypt_password(encrypted_password):
    key = os.getenv("FERNET_KEY")
    fernet = Fernet(key.encode())
    return fernet.decrypt(encrypted_password.encode()).decode()
