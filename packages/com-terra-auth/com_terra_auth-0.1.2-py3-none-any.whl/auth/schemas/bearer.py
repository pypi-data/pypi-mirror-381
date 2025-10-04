from fastapi import HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from typing import Optional

class HTTPBearer401(HTTPBearer):
    """
    Custom HTTPBearer that returns 401 on missing or invalid credentials,
    and logs unauthorized access attempts.
    """

    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials:
        try:
            credentials: Optional[HTTPAuthorizationCredentials] = await super().__call__(request)

            if not credentials:
                print("Unauthorized request: credentials not found")
                raise HTTPException(status_code=401, detail="Unauthorized")
            
            return credentials

        except HTTPException as he:
            if he.status_code == 401:
                print(f"Unauthorized request: {he.detail}")
                raise HTTPException(status_code=401, detail="Unauthorized")
            raise he