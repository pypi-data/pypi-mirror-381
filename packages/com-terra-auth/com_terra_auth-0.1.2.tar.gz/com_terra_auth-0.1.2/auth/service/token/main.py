from inspect import iscoroutine
from datetime import datetime, timedelta, timezone
from typing import Callable, List, Optional
from uuid import uuid4

from fastapi import HTTPException
from jose import JWTError
from jose.constants import Algorithms, ALGORITHMS

from ...config import EncDecConfig
from ...schemas import JwtClaims
from ..jwt import sign, verify
from ..jwe import encrypt, decrypt
from ..fernet import encrypt as fernet_encrypt, decrypt as fernet_decrypt

async def handle_resolve_key(fn: Callable[..., str]) -> str:
    return await fn(...) if iscoroutine(fn) else fn(...)

def token_create(payload: dict, sign_key: str, minutes: int = 5, sign_algorithm: Algorithms = ALGORITHMS.RS256, encryption_config: Optional[EncDecConfig] = None) -> str:
    """Create a signed JWT and return a Token with only the scoped fields."""
    try:
        # Basic validation (internal only)
        if "sub" not in payload:
            print("Token creation failed: missing 'sub' claim.")
            raise ValueError("Missing subject claim")

        sub = str(payload["sub"])
        now = datetime.now(tz=timezone.utc)
        exp = (now + timedelta(minutes=minutes)).timestamp()
        iat = int(now.timestamp())
        jti = str(uuid4())

        claims = JwtClaims(sub=sub,exp=exp, iat=iat, jti=jti, payload=payload)
        claims_dict = claims.model_dump()

        # Step 1: Sign the token
        signed_jwt = sign(claims=claims_dict, key=sign_key, algorithm=sign_algorithm)
        
        # Step 2: Optional Encryption
        if encryption_config:
            enc_type = encryption_config.type
            enc_key = encryption_config.key
            enc_alg = encryption_config.algorithm

            if not enc_key:
                print("Encryption config provided without key.")
                raise ValueError("Missing encryption key")

            if enc_type == "jwe":
                return encrypt(plaintext=signed_jwt, key=enc_key, encryption=enc_alg)
            elif enc_type == "fernet":
                return fernet_encrypt(plaintext=signed_jwt, key=enc_key)
            else:
                print(f"Unsupported encryption type: {enc_type}")
                raise ValueError("Unsupported encryption type")

        # Create Token
        return signed_jwt


    except HTTPException:
        raise  # Only 401/403 pass through if ever added later
    except Exception as e:
        # Log but hide from client
        print(f"Token creation failed: {e}")
        raise HTTPException(status_code=500, detail="Unable to create session")

def token_verify(token: str, sign_key: str, sign_algorithms: List[Algorithms] = [ALGORITHMS.RS256], decryption_config: Optional[EncDecConfig] = None) -> dict:
    """Verify and optionally decrypt a token."""

    try:
        # Step 1: Optional Decryption
        if decryption_config:
            dec_type = decryption_config.type
            dec_key = decryption_config.key

            if not dec_key:
                print("Decryption config missing key.")
                raise ValueError("Missing decryption key")

            if dec_type == "jwe":
                token = decrypt(ciphertext=token, key=dec_key)
            elif dec_type == "fernet":
                token = fernet_decrypt(ciphertext=token, key=dec_key)
            else:
                print(f"Unsupported decryption type: {dec_type}")
                raise ValueError("Unsupported decryption type")

        # Step 2: Verify signature
        return verify(token=token, key=sign_key, algorithms=sign_algorithms)

    except JWTError:
        # Auth failure — valid to expose
        raise HTTPException(status_code=401, detail="Unauthorized")
    except HTTPException:
        raise  # Pass through only 401/403
    except Exception as e:
        # Everything else: safe internal log
        print(f"Unexpected verification error: {e}")
        raise HTTPException(status_code=401, detail="Unauthorized.")

def token_validate(claims: dict, purpose: str) -> bool:
    """Validate claims and intended purpose."""
    try:
        jti = claims.get("jti")
        payload = claims.get("payload", {})

        if not jti or payload.get("purpose") != purpose:
            return False

        # Optional: check blacklist or revoked token store
        return True

    except Exception as e:
        print(f"Unexpected validation error: {e}")
        raise HTTPException(status_code=401, detail="Unauthorized.")
