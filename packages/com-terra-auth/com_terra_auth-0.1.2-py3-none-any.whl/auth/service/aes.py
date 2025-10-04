import os
import base64

from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def generate_aes_key() -> bytes:
    return os.urandom(32)
    
def encrypt_payload(plaintext: str, aes: bytes) -> str:
    """Encrypt payload using AES-GCM, returns base64 ciphertext including nonce."""
    
    try:
        if not aes:
            raise ValueError("AES key required")
        
        aesgcm = AESGCM(aes)
        nonce = os.urandom(12) # ensures uniqueness and prevents nonce reuse attacks
        ciphertext = aesgcm.encrypt(nonce, plaintext.encode(), associated_data=None)
        
        return base64.b64encode(nonce + ciphertext).decode("utf-8")
    
    except Exception as e:
        raise ValueError(f"AES payload encryption failed: {str(e)}")

def decrypt_payload(b64_ciphertext: str, aes: bytes) -> str:
    """Decrypt base64 ciphertext using AES-GCM."""

    try:
        if not aes:
            raise ValueError("AES key required")
        raw = base64.b64decode(b64_ciphertext)
        nonce, ciphertext = raw[:12], raw[12:]
        aesgcm = AESGCM(aes)
        plaintext = aesgcm.decrypt(nonce, ciphertext, associated_data=None)
        return plaintext.decode("utf-8")
    
    except Exception as e:
        raise ValueError(f"AES payload decryption failed: {str(e)}")
    
def encrypt_aes(aes: bytes, pub: str) -> str:
    """Encrypt AES key with RSA public key."""
    
    if not aes or not pub:
        raise ValueError("AES key and RSA public key required")
    
    try:
        public_key = serialization.load_pem_public_key(pub.encode())
        encrypted_aes_key = public_key.encrypt(
            aes,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return base64.b64encode(encrypted_aes_key).decode("utf-8")
    
    except Exception as e:
        raise ValueError(f"RSA AES encryption failed: {str(e)}")

def decrypt_aes(encrypted_aes: str, priv: str) -> bytes:
    """Decrypt AES key with RSA private key."""
    
    if not encrypted_aes or not priv:
        raise ValueError("Encrypted AES key and RSA private key required")

    try:
        private_key = serialization.load_pem_private_key(priv.encode(), password=None)
        encrypted_bytes = base64.b64decode(encrypted_aes)
        return private_key.decrypt(
            encrypted_bytes,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
    
    except Exception as e:
        raise ValueError(f"RSA AES decryption failed: {str(e)}")