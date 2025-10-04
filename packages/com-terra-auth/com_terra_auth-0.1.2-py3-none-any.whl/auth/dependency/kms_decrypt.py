import json
from typing import Any, Callable, Optional, Type

from fastapi import Depends, Request, HTTPException
from pydantic import BaseModel

from ..service.aws.kms import decrypt
from ..schemas import EncryptedPayload

"""
USAGE:
@router.post("/signin")
async def handle_singin(payload: SignInPayload = KMSDecrypt(boto3_client_dep=get_aws_kms_client, key_id=KMS_KEY_ID, model=SignInPayload)):
    return await singin(payload)
"""
def KMSDecrypt(
    boto3_client_dep: callable,
    key_id: str,
    encryption_algorithm: str = "RSAES_OAEP_SHA_256",
    model: Optional[Type[BaseModel]] = None
) -> Callable[[Request], Any]:
    """
    FastAPI dependency to decrypt an incoming encrypted payload.

    Args:
        boto3_client_dep: KMS client instance.
        key_id: KMS key ID to use for decryption.
        encryption_algorithm: Optional, defaults to "RSAES_OAEP_SHA_256".
        model: Optional Pydantic model class to parse decrypted payload.

    Returns:
        A FastAPI dependency that provides decrypted data either as dict or BaseModel instance.
    """
    
    async def dependency(payload: EncryptedPayload, boto3_client = Depends(boto3_client_dep)) -> Any:
        print(boto3_client)
        try:
            encrypted_payload = payload.encryptedPayload
            if not encrypted_payload:
                raise HTTPException(status_code=400, detail="Missing 'encryptedPayload' field")

            # Decrypt payload
            plaintext = await decrypt(boto3_client, key_id, encrypted_payload, encryption_algorithm)

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
