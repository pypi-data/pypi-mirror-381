from typing import Literal, Optional
from pydantic import BaseModel, ConfigDict

class EncDecConfig(BaseModel):
    type: Literal["jwe", "fernet"]
    key: str
    algorithm: Optional[str] = None

    model_config = ConfigDict(from_attributes=True, extra="forbid")
