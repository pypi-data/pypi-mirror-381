from cryptography.fernet import Fernet, InvalidToken

def encrypt(plaintext: str, key: str) -> str:
    try:
        fernet: Fernet = Fernet(key)
        token_bytes = fernet.encrypt(plaintext.encode("utf-8"))
        return token_bytes.decode("utf-8")
    except Exception as e:
        raise ValueError(f"Fernet encryption failed: {str(e)}")

def decrypt(ciphertext: str, key: str) -> str:
    try:
        fernet: Fernet = Fernet(key)
        decrypted_bytes = fernet.decrypt(ciphertext.encode("utf-8"))
        return decrypted_bytes.decode("utf-8")
    except InvalidToken:
        raise ValueError("Fernet decryption failed: Invalid token")
    except Exception as e:
        raise ValueError(f"Fernet decryption failed: {str(e)}")

def generate_key() -> str:
    return Fernet.generate_key().decode("utf-8")
