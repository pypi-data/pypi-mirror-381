from pydantic import BaseModel

class EncryptedPayload(BaseModel):
    encryptedPayload: str