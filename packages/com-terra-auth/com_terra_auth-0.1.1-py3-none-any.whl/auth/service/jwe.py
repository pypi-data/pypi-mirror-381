from jose import jwe, JWTError
from jose.constants import Algorithms, ALGORITHMS

def encrypt(plaintext: str, key: str, encryption: Algorithms = ALGORITHMS.A256GCM) -> str:
    try:
        token_bytes = jwe.encrypt(plaintext=plaintext, key=key, algorithm="dir", encryption=encryption)
        return token_bytes.decode("utf-8")
    except JWTError as e:
        raise ValueError(f"JWE encryption failed: {str(e)}")

def decrypt(ciphertext: str, key: str) -> str:
    try:
        decrypted_bytes = jwe.decrypt(jwe_str=ciphertext, key=key)
        return decrypted_bytes.decode("utf-8")
    except JWTError as e:
        raise ValueError(f"JWE decryption failed: {str(e)}")
