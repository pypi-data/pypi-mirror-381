from typing import Any
import boto3

_aws_client: Any = None

def create_session() -> boto3.Session:
    return boto3.Session()

def register_client(session: boto3.Session, service_name: str, region_name: str) -> None:
    global _aws_client
    _aws_client = session.client(service_name, region_name=region_name)

def get_client() -> Any:
    if _aws_client is None:
        raise RuntimeError("AWS client not initialized. Call init_aws_client() first.")
    return _aws_client
