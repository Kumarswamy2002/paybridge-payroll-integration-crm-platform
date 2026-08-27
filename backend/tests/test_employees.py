import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_employee_crm_flow(client: AsyncClient):
    # 1. Setup Tenant and User
    tenant_res = await client.post("/api/v1/tenants/", json={"name": "Nexus", "slug": "nexus"})
    tenant_id = tenant_res.json()["id"]

    reg_res = await client.post("/api/v1/auth/register", json={
        "email": "hr@nexus.com",
        "password": "Password123!",
        "full_name": "HR Lead",
        "tenant_id": tenant_id,
        "role": "HR_MANAGER"
    })

    login_res = await client.post("/api/v1/auth/login", json={
        "email": "hr@nexus.com",
        "password": "Password123!",
        "tenant_slug": "nexus"
    })
    token = login_res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 2. Create Organization and Department
    org_res = await client.post("/api/v1/orgs/orgs", json={"name": "Nexus Corp"}, headers=headers)
    org_id = org_res.json()["id"]

    dept_res = await client.post("/api/v1/orgs/departments", json={
        "organization_id": org_id,
        "name": "Engineering"
    }, headers=headers)
    dept_id = dept_res.json()["id"]

    # 3. Create Employee
    emp_res = await client.post("/api/v1/employees/", json={
        "employee_code": "EMP-001",
        "first_name": "Sarah",
        "last_name": "Connor",
        "email": "sarah.c@nexus.com",
        "department_id": dept_id,
        "employment_type": "FULL_TIME"
    }, headers=headers)
    assert emp_res.status_code == 200
    emp_data = emp_res.json()
    emp_id = emp_data["id"]

    # 4. Create Payroll Profile
    payroll_res = await client.post("/api/v1/payroll/profiles", json={
        "employee_id": emp_id,
        "payroll_provider": "GUSTO",
        "external_provider_employee_id": "GUSTO-9921"
    }, headers=headers)
    assert payroll_res.status_code == 200

    # 5. Create Compensation
    comp_res = await client.post("/api/v1/payroll/compensation", json={
        "employee_id": emp_id,
        "pay_frequency": "MONTHLY",
        "currency": "USD",
        "base_salary": 125000.00,
        "effective_date": "2026-01-01"
    }, headers=headers)
    assert comp_res.status_code == 200

    # 6. Fetch Employee 360 View
    e360_res = await client.get(f"/api/v1/employees/{emp_id}/360", headers=headers)
    assert e360_res.status_code == 200
    e360 = e360_res.json()
    assert e360["employee"]["first_name"] == "Sarah"
    assert e360["department_name"] == "Engineering"
    assert e360["payroll_provider"] == "GUSTO"
    assert e360["base_salary"] == 125000.00

    # 7. Check Unified CRM Timeline
    timeline_res = await client.get(f"/api/v1/crm/timeline/{emp_id}", headers=headers)
    assert timeline_res.status_code == 200
    events = timeline_res.json()
    assert len(events) >= 3  # EMPLOYEE_CREATED, PAYROLL_PROFILE_CREATED, SALARY_UPDATED
