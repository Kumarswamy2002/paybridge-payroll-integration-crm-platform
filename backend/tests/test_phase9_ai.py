import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_ai_payroll_intelligence_endpoints(client: AsyncClient):
    # 1. Setup Tenant and User
    tenant_res = await client.post("/api/v1/tenants/", json={"name": "AILabs", "slug": "ailabs"})
    tenant_id = tenant_res.json()["id"]

    reg_res = await client.post("/api/v1/auth/register", json={
        "email": "ai_lead@ailabs.com",
        "password": "Password123!",
        "full_name": "AI Lead",
        "tenant_id": tenant_id,
        "role": "TENANT_ADMIN"
    })
    headers = {"Authorization": f"Bearer {(await client.post('/api/v1/auth/login', json={'email': 'ai_lead@ailabs.com', 'password': 'Password123!', 'tenant_slug': 'ailabs'})).json()['access_token']}"}

    # Create Employee & Case
    emp_res = await client.post("/api/v1/employees/", json={
        "employee_code": "EMP-AI-01",
        "first_name": "Alan",
        "last_name": "Turing",
        "email": "alan.t@ailabs.com"
    }, headers=headers)
    emp_id = emp_res.json()["id"]

    case_res = await client.post("/api/v1/crm/cases", json={
        "employee_id": emp_id,
        "title": "Tax Withholding Discrepancy",
        "category": "TAX_QUERY",
        "priority": "HIGH"
    }, headers=headers)
    case_id = case_res.json()["id"]

    # 2. AI Case Summarization
    sum_res = await client.post("/api/v1/ai/summarize-case", json={"case_id": case_id}, headers=headers)
    assert sum_res.status_code == 200
    sum_data = sum_res.json()
    assert sum_data["case_id"] == case_id
    assert "Tax Withholding Discrepancy" in sum_data["title"]
    assert len(sum_data["recommended_actions"]) >= 1

    # 3. AI Anomaly Detection
    anomaly_res = await client.post("/api/v1/ai/detect-anomalies", json={
        "payroll_run_data": [
            {"external_employee_id": "EMP-101", "gross_pay": 15000.0, "expected_gross": 10000.0}, # 50% spike!
            {"external_employee_id": "EMP-102", "gross_pay": 10000.0, "expected_gross": 10000.0}
        ]
    }, headers=headers)
    assert anomaly_res.status_code == 200
    anom_data = anomaly_res.json()
    assert anom_data["anomalies_detected_count"] == 1
    assert anom_data["anomalies"][0]["anomaly_type"] == "HIGH_SALARY_VARIANCE"

    # 4. Natural Language Query
    query_res = await client.post("/api/v1/ai/query", json={
        "prompt": "Why did employee synchronization fail yesterday?"
    }, headers=headers)
    assert query_res.status_code == 200
    query_data = query_res.json()
    assert "answer" in query_data
