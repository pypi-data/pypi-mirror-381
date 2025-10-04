from typing import Callable, Dict, List, Optional
from inspect import iscoroutine

from fastapi import Request, Depends
from fastapi.security import HTTPAuthorizationCredentials

from jose.constants import Algorithms, ALGORITHMS

from ..config import EncDecConfig
from ..service.token import token_verify
from ..schemas import HTTPBearer401, AuthContext, JwtClaims

bearer_scheme = HTTPBearer401()

async def handle_resolve_key(fn: Callable[..., str], *args, **kwargs) -> str:
    result = fn(*args, **kwargs)
    if iscoroutine(result):
        result = await result
    return result

def Authorize(
    key: Optional[str] = None, # Pass a static key
    resolve_key: Optional[Callable[..., str]] = None, # Pass a resolver function

    algorithms: List[Algorithms] = [ALGORITHMS.RS256],
    decryption_config: Optional[EncDecConfig] = None, # Optional decryption config (fernet/jwe)
    roles: Optional[Dict] = None # Optional role permissions mapping dict
):

    if not key and not resolve_key:
        raise ValueError("Either key or resolve_key must be provided")

    if roles is None:
        roles = {}

    async def dependency(
        _: Request, 
        authorization: HTTPAuthorizationCredentials = Depends(bearer_scheme)
    ) -> AuthContext:        
        # resolve key here (inside async context)
        verification_key: str = key
        if not verification_key and resolve_key:
            verification_key = await handle_resolve_key(resolve_key)

        # Get token
        token: str = authorization.credentials

        # Verify + decrypt token if needed
        claims_dict: dict = token_verify(
            token=token,
            key=verification_key,
            algorithms=algorithms,
            decryption_config=decryption_config
        )
        claims: JwtClaims = JwtClaims(**claims_dict)
        
        # verify role permissions
        payload_dict: dict = claims.payload
        
        # Pass auth context info to the route if needed
        auth_context: AuthContext = AuthContext(
            payload=payload_dict,
            jti=claims.jti
        )

        return auth_context

    return Depends(dependency)