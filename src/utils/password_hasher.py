import hashlib

def hash_password(password: str) -> str:
    hased_password = hashlib.sha256(password.encode('UTF-8'))
    return hased_password.hexdigest()
   