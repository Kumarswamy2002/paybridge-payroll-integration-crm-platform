import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_reconciliation_and_exception_to_crm_pipeline(client: AsyncClient):
    # 1. Setup Tenant and User
    tenant_res = await client.post("/api/v1/tenants/", json={"name": "Polaris Corp", "slug": "polaris"})
    tenant_id = tenant_res.json()["id"]

    reg_res = await client.post("/api/v1/auth/register", json={
        "email": "lead@polaris.com",
        "password": "Password123!",
        "full_name": "Payroll Officer",
        "tenant_id": tenant_id,
        "role": "PAYROLL_ADMIN"
    })
    headers = {"Authorization": f"Bearer {(await client.post('/api/v1/auth/login', json={'email': 'lead@polaris.com', 'password': 'Password123!', 'tenant_slug': 'polaris'})).json()['access_token']}"}

    # 2. Create Employee
    emp_res = await client.post("/api/v1/employees/", json={
        "employee_code": "EMP-POL-100",
        "first_name": "Claire",
        "last_name": "Redfield",
        "email": "claire.r@polaris.com"
    }, headers=headers)
    emp_id = emp_res.json()["id"]

    # 3. Create Payroll Profile (Gusto ID: GUSTO-CLAIRE-100)
    await client.post("/api/v1/payroll/profiles", json={
        "employee_id": emp_id,
        "payroll_provider": "GUSTO",
        "external_provider_employee_id": "GUSTO-CLAIRE-100"
    }, headers=headers)

    # 4. Create Active Compensation ($120,000 / yr = $10,000 / month)
    await client.post("/api/v1/payroll/compensation", json={
        "employee_id": emp_id,
        "pay_frequency": "MONTHLY",
        "currency": "USD",
        "base_salary": 120000.0,
        "effective_date": "2026-01-01"
    }, headers=headers)

    # 5. Trigger Reconciliation with Mismatching Provider Result ($8,500 gross instead of $10,000)
    provider_results = [
        {
            "payroll_run_id": "GUSTO-RUN-JAN-2026",
            "external_employee_id": "GUSTO-CLAIRE-100",
            "gross_pay": 8500.00,  # $1,500 mismatch!
            "net_pay": 6200.00,
            "tax_withheld": 1800.00,
            "deductions": 500.00,
            "direct_deposit_amount": 6200.00
        }
    ]

    recon_res = await client.post("/api/v1/reconciliation/run", json={
        "payroll_provider": "GUSTO",
        "payroll_run_id": "GUSTO-RUN-JAN-2026",
        "provider_results": provider_results,
        "tolerance_threshold": 1.00
    }, headers=headers)
    assert recon_res.status_code == 200
    recon_data = recon_res.json()
    assert recon_data["total_compared"] == 1
    assert recon_data["discrepancies_count"] == 1

    # 6. Verify Discrepancies List API
    discrepancies_res = await client.get("/api/v1/reconciliation/discrepancies", headers=headers)
    assert discrepancies_res.status_code == 200
    discrepancies = discrepancies_res.json()
    assert len(discrepancies) >= 1
    disc = discrepancies[0]
    assert disc["discrepancy_type"] == "SALARY_MISMATCH"
    assert disc["variance_amount"] == 1500.00
    assert disc["status"] == "CASE_CREATED"
    assert disc["crm_case_id"] is not None

    # 7. Verify Auto-Created CRM Exception Ticket
    cases_res = await client.get(f"/api/v1/crm/cases?employee_id={emp_id}", headers=headers)
    assert cases_res.status_code == 200
    cases = cases_res.json()
    assert len(cases) >= 1
    case = cases[0]
    assert case["id"] == disc["crm_case_id"]
    assert "Reconciliation Mismatch" in case["title"]
    assert case["category"] == "DISCREPANCY"
    assert case["priority"] == "HIGH"
