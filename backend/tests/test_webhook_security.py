import time
from backend.app.core.webhook_security import WebhookSecurityManager

def test_webhook_hmac_sign_and_verify():
    secret = "whsec_test_secret_123"
    payload = '{"event": "payroll.completed", "id": "pr_999"}'
    ts = int(time.time())
    sig = WebhookSecurityManager.generate_signature(payload, secret, ts)
    assert WebhookSecurityManager.verify_signature(payload, sig, secret) is True
    assert WebhookSecurityManager.verify_signature(payload, sig, "wrong_secret") is False

def test_backoff_delay():
    assert WebhookSecurityManager.compute_backoff_delay(1) == 1.0
    assert WebhookSecurityManager.compute_backoff_delay(2) == 2.0
    assert WebhookSecurityManager.compute_backoff_delay(3) == 4.0
