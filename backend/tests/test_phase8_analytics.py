import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_analytics_platform_endpoints(client: AsyncClient):
    # 1. Setup Tenant and User
    tenant_res = await client.post("/api/v1/tenants/", json={"name": "AnalyticsCorp", "slug": "analyticscorp"})
    tenant_id = tenant_res.json()["id"]

    reg_res = await client.post("/api/v1/auth/register", json={
        "email": "analyst@analyticscorp.com",
        "password": "Password123!",
        "full_name": "Data Lead",
        "tenant_id": tenant_id,
        "role": "TENANT_ADMIN"
    })
    headers = {"Authorization": f"Bearer {(await client.post('/api/v1/auth/login', json={'email': 'analyst@analyticscorp.com', 'password': 'Password123!', 'tenant_slug': 'analyticscorp'})).json()['access_token']}"}

    # Create 2 employees with active compensation
    e1_res = await client.post("/api/v1/employees/", json={
        "employee_code": "EMP-ANA-01",
        "first_name": "Carl",
        "last_name": "Sagan",
        "email": "carl.s@analyticscorp.com"
    }, headers=headers)
    e1_id = e1_res.json()["id"]

    await client.post("/api/v1/payroll/compensation", json={
        "employee_id": e1_id,
        "base_salary": 180000.0,
        "effective_date": "2026-01-01"
    }, headers=headers)

    # 2. Executive Overview Endpoint
    over_res = await client.get("/api/v1/analytics/overview", headers=headers)
    assert over_res.status_code == 200
    overview = over_res.json()
    assert overview["active_employees"] >= 1
    assert overview["annual_payroll_commitment"] == 180000.0
    assert overview["monthly_payroll_commitment"] == 15000.0

    # 3. Sync Performance Endpoint
    sync_res = await client.get("/api/v1/analytics/sync-performance", headers=headers)
    assert sync_res.status_code == 200
    sync_data = sync_res.json()
    assert "sync_success_rate" in sync_data

    # 4. Cases SLA Endpoint
    sla_res = await client.get("/api/v1/analytics/cases-sla", headers=headers)
    assert sla_res.status_code == 200
    sla_data = sla_res.json()
    assert "sla_compliance_rate" in sla_data
