import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_create_and_get_tenant(client: AsyncClient):
    # 1. Create Tenant
    tenant_payload = {
        "name": "Acme Corp",
        "slug": "acme-corp",
        "domain": "acme.com",
        "subscription_plan": "ENTERPRISE"
    }
    response = await client.post("/api/v1/tenants/", json=tenant_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Acme Corp"
    assert data["slug"] == "acme-corp"
    assert "id" in data

    # 2. Get Tenant by Slug
    response_slug = await client.get("/api/v1/tenants/slug/acme-corp")
    assert response_slug.status_code == 200
    assert response_slug.json()["id"] == data["id"]
