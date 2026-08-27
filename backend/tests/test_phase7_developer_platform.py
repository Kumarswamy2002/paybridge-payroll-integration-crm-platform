import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_developer_platform_and_webhook_gateway(client: AsyncClient):
    # 1. Setup Tenant and Admin User
    tenant_res = await client.post("/api/v1/tenants/", json={"name": "DevCorp", "slug": "devcorp"})
    tenant_id = tenant_res.json()["id"]

    reg_res = await client.post("/api/v1/auth/register", json={
        "email": "dev_admin@devcorp.com",
        "password": "Password123!",
        "full_name": "Dev Admin",
        "tenant_id": tenant_id,
        "role": "TENANT_ADMIN"
    })
    headers = {"Authorization": f"Bearer {(await client.post('/api/v1/auth/login', json={'email': 'dev_admin@devcorp.com', 'password': 'Password123!', 'tenant_slug': 'devcorp'})).json()['access_token']}"}

    # 2. Create Scoped API Key
    key_res = await client.post("/api/v1/developers/api-keys", json={
        "name": "Integration Service Key",
        "scopes": ["employees:read", "payroll:write"]
    }, headers=headers)
    assert key_res.status_code == 200
    key_data = key_res.json()
    assert "pb_live_" in key_data["api_key"]
    assert key_data["scopes"] == ["employees:read", "payroll:write"]

    # 3. List Tenant API Keys
    list_res = await client.get("/api/v1/developers/api-keys", headers=headers)
    assert list_res.status_code == 200
    keys = list_res.json()
    assert len(keys) >= 1
    assert keys[0]["name"] == "Integration Service Key"

    # 4. Incoming Webhook Gateway Execution (First call: PROCESSED)
    webhook_payload = {
        "event_id": "wh_evt_9001",
        "event_type": "employee.updated",
        "employee_id": "gusto_emp_8801",
        "timestamp": "2026-02-01T12:00:00Z"
    }
    wh_headers = {"x-idempotency-key": "wh_evt_9001", "x-signature": "valid_demo_sig"}

    wh1_res = await client.post(
        "/api/v1/developers/webhooks/incoming/GUSTO", 
        json=webhook_payload, 
        headers=wh_headers
    )
    assert wh1_res.status_code == 200
    assert wh1_res.json()["status"] == "PROCESSED"

    # 5. Duplicate Webhook Execution (Second call with same Idempotency Key: DUPLICATE_IGNORED)
    wh2_res = await client.post(
        "/api/v1/developers/webhooks/incoming/GUSTO", 
        json=webhook_payload, 
        headers=wh_headers
    )
    assert wh2_res.status_code == 200
    assert wh2_res.json()["status"] == "DUPLICATE_IGNORED"
