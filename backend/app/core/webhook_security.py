"""
Webhook Security & HMAC-SHA256 Signature Verification
"""
import hmac
import hashlib
import time
from typing import Dict, Any

class WebhookSecurityManager:
    @staticmethod
    def generate_signature(payload: str, secret: str, timestamp: int) -> str:
        data = f"t={timestamp}.v1={payload}".encode('utf-8')
        sig = hmac.new(secret.encode('utf-8'), data, hashlib.sha256).hexdigest()
        return f"t={timestamp},v1={sig}"

    @staticmethod
    def verify_signature(payload: str, header_sig: str, secret: str, tolerance_sec: int = 300) -> bool:
        try:
            parts = dict(x.split('=') for x in header_sig.split(','))
            timestamp = int(parts['t'])
            received_sig = parts['v1']
            if abs(time.time() - timestamp) > tolerance_sec:
                return False
            expected = WebhookSecurityManager.generate_signature(payload, secret, timestamp).split('v1=')[1]
            return hmac.compare_digest(received_sig, expected)
        except Exception:
            return False

    @staticmethod
    def compute_backoff_delay(attempt: int, base_delay: float = 1.0, max_delay: float = 60.0) -> float:
        delay = base_delay * (2 ** (attempt - 1))
        return min(delay, max_delay)
