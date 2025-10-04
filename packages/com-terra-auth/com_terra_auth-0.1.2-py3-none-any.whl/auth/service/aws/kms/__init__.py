import base64
from typing import Any

async def fetch_pubkey(client: Any, key_id: str) -> str:
    response = client.get_public_key(KeyId=key_id)
    public_key_der = response["PublicKey"]

    # Convert DER → PEM
    public_key_b64 = base64.b64encode(public_key_der).decode("utf-8")
    public_key_pem = "-----BEGIN PUBLIC KEY-----\n"
    public_key_pem += "\n".join(
        [public_key_b64[i:i + 64] for i in range(0, len(public_key_b64), 64)]
    )
    public_key_pem += "\n-----END PUBLIC KEY-----"

    return public_key_pem

async def decrypt(
    boto3_client: Any,
    kms_keyid: str,
    encrypted_payload: str,
    encryption_algorithm: str = "RSAES_OAEP_SHA_256",
) -> str:
    ciphertext_blob = base64.b64decode(encrypted_payload)
    response = boto3_client.decrypt(
        KeyId=kms_keyid,
        CiphertextBlob=ciphertext_blob,
        EncryptionAlgorithm=encryption_algorithm,
    )
    return response["Plaintext"].decode("utf-8")
