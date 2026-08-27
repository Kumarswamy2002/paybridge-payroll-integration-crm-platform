import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_user_registration_and_login(client: AsyncClient):
    # 1. Create Tenant first
    tenant_res = await client.post("/api/v1/tenants/", json={
        "name": "Global Tech",
        "slug": "global-tech"
    })
    tenant_id = tenant_res.json()["id"]

    # 2. Register user
    user_payload = {
        "email": "admin@globaltech.com",
        "password": "SecurePassword123!",
        "full_name": "Tech Admin",
        "tenant_id": tenant_id,
        "role": "TENANT_ADMIN"
    }
    reg_res = await client.post("/api/v1/auth/register", json=user_payload)
    assert reg_res.status_code == 200
    assert reg_res.json()["email"] == "admin@globaltech.com"

    # 3. Login user
    login_payload = {
        "email": "admin@globaltech.com",
        "password": "SecurePassword123!",
        "tenant_slug": "global-tech"
    }
    login_res = await client.post("/api/v1/auth/login", json=login_payload)
    assert login_res.status_code == 200
    token_data = login_res.json()
    assert "access_token" in token_data
    assert token_data["role"] == "TENANT_ADMIN"
