import base64
import os
from cryptography.fernet import Fernet
from app.core.config import settings

def _get_fernet() -> Fernet:
    # Ensure key is valid Fernet key (32 url-safe base64-encoded bytes)
    key_bytes = settings.PII_ENCRYPTION_KEY.encode()
    # Hash or pad to 32 bytes then base64 encode
    b64_key = base64.urlsafe_b64encode(key_bytes.ljust(32)[:32])
    return Fernet(b64_key)

def encrypt_field(plain_text: str) -> str:
    """Encrypt sensitive PII string using AES-Fernet."""
    if not plain_text:
        return ""
    fernet = _get_fernet()
    return fernet.encrypt(plain_text.encode()).decode()

def decrypt_field(cipher_text: str) -> str:
    """Decrypt sensitive PII string."""
    if not cipher_text:
        return ""
    try:
        fernet = _get_fernet()
        return fernet.decrypt(cipher_text.encode()).decode()
    except Exception:
        return cipher_text  # Fallback if not encrypted
