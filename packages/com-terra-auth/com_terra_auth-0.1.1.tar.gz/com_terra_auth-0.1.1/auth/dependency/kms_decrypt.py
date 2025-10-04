import json
from typing import Any, Callable, Optional, Type

from fastapi import Depends, Request, HTTPException
from pydantic import BaseModel

from ..service.aws.kms import decrypt

def KMSDecrypt(
    boto3_client,
    kms_keyid: str,
    encryption_algorithm: str = "RSAES_OAEP_SHA_256",
    model: Optional[Type[BaseModel]] = None
) -> Callable[[Request], Any]:
    """
    FastAPI dependency to decrypt an incoming encrypted payload.

    Args:
        client: KMS client instance.
        kms_keyid: KMS key ID to use for decryption.
        encryption_algorithm: Optional, defaults to "RSAES_OAEP_SHA_256".
        model: Optional Pydantic model class to parse decrypted payload.

    Returns:
        A FastAPI dependency that provides decrypted data either as dict or BaseModel instance.
    """
    async def dependency(request: Request) -> Any:
        try:
            body_bytes = await request.body()
            if not body_bytes:
                raise HTTPException(status_code=400, detail="Empty request body")

            try:
                body_json = json.loads(body_bytes)
            except json.JSONDecodeError:
                raise HTTPException(status_code=400, detail="Invalid JSON body")

            encrypted_payload = body_json.get("encryptedPayload")
            if not encrypted_payload:
                raise HTTPException(status_code=400, detail="Missing 'encryptedPayload' field")

            # Decrypt payload
            plaintext = await decrypt(boto3_client, kms_keyid, encrypted_payload, encryption_algorithm)

            # Try parsing plaintext as JSON
            try:
                decrypted_dict = json.loads(plaintext)
            except (json.JSONDecodeError, TypeError):
                decrypted_dict = {"plaintext": plaintext}

            # Return as BaseModel if requested
            if model is not None:
                try:
                    return model(**decrypted_dict)
                except Exception as e:
                    raise HTTPException(status_code=400, detail=f"Invalid decrypted data for model: {str(e)}")

            return decrypted_dict

        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Decryption failed: {str(e)}")

    return Depends(dependency)
