# from typing import Optional
from pydantic import BaseModel

class AuthContext(BaseModel):
    payload: dict
    jti: str
    # token: Optional[str] = None