from jose import jwt, JWTError
from jose.constants import ALGORITHMS

def sign(claims: dict, key: str, algorithm: str = ALGORITHMS.RS256) -> str:
    try:
        token = jwt.encode(claims=claims, key=key, algorithm=algorithm)
        return token
    except JWTError as e:
        raise ValueError(f"JWS signing failed: {str(e)}")

def verify(token: str, key: str, algorithms: list[str] = [ALGORITHMS.RS256]) -> dict:
    try:
        payload = jwt.decode(token=token, key=key, algorithms=algorithms)
        return payload
    except JWTError as e:
        raise ValueError(f"JWS verification failed: {str(e)}")
