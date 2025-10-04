from typing import Any
from pydantic import BaseModel, ConfigDict

class KMSConfig(BaseModel):
    key_id: str
    client: Any

    model_config = ConfigDict(arbitrary_types_allowed=True)
