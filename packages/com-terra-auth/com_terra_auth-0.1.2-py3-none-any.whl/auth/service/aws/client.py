from typing import Any
import boto3

def create_session() -> boto3.Session:
    return boto3.Session()

def register_client(session: boto3.Session, service_name: str, region_name: str) -> Any:
    return session.client(service_name, region_name=region_name)
