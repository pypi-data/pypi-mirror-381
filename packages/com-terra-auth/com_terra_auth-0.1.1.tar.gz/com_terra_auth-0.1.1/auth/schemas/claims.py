from pydantic import BaseModel, ConfigDict

class JwtClaims(BaseModel):
    sub: str
    jti: str
    iat: float
    exp: float
    payload: dict

    model_config = ConfigDict(from_attributes=True, extra="forbid")