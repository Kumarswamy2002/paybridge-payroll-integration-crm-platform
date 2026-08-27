import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_notification_and_case_messaging_flow(client: AsyncClient):
    # 1. Setup Tenant and User
    tenant_res = await client.post("/api/v1/tenants/", json={"name": "OmniCorp", "slug": "omnicorp"})
    tenant_id = tenant_res.json()["id"]

    reg_res = await client.post("/api/v1/auth/register", json={
        "email": "employee@omnicorp.com",
        "password": "Password123!",
        "full_name": "Robo Cop",
        "tenant_id": tenant_id,
        "role": "EMPLOYEE"
    })
    user_id = reg_res.json()["id"]

    login_res = await client.post("/api/v1/auth/login", json={
        "email": "employee@omnicorp.com",
        "password": "Password123!",
        "tenant_slug": "omnicorp"
    })
    headers = {"Authorization": f"Bearer {login_res.json()['access_token']}"}

    # 2. Send Template Notification
    send_res = await client.post("/api/v1/notifications/send", json={
        "user_id": user_id,
        "title": "January Payslip Published",
        "template_name": "PAYSLIP_AVAILABLE",
        "context": {"name": "Robo Cop", "period": "January 2026"}
    }, headers=headers)
    assert send_res.status_code == 200
    notif_data = send_res.json()
    notif_id = notif_data["id"]
    assert "Robo Cop" in notif_data["message"]
    assert notif_data["is_read"] is False

    # 3. List My Notifications
    my_notif_res = await client.get("/api/v1/notifications/", headers=headers)
    assert my_notif_res.status_code == 200
    assert len(my_notif_res.json()) >= 1

    # 4. Mark as Read
    read_res = await client.post(f"/api/v1/notifications/{notif_id}/read", headers=headers)
    assert read_res.status_code == 200
    assert read_res.json()["is_read"] is True

    # 5. Case Message Threading Flow
    emp_res = await client.post("/api/v1/employees/", json={
        "employee_code": "EMP-OMNI-01",
        "first_name": "Robo",
        "last_name": "Cop",
        "email": "employee@omnicorp.com"
    }, headers=headers)
    emp_id = emp_res.json()["id"]

    case_res = await client.post("/api/v1/crm/cases", json={
        "employee_id": emp_id,
        "title": "W2 Form Copy Request",
        "category": "TAX_QUERY"
    }, headers=headers)
    case_id = case_res.json()["id"]

    # Post Message to Case
    msg_res = await client.post(f"/api/v1/notifications/cases/{case_id}/messages", json={
        "content": "Please send my 2025 W2 tax document PDF.",
        "message_type": "PUBLIC"
    }, headers=headers)
    assert msg_res.status_code == 200
    assert msg_res.json()["content"] == "Please send my 2025 W2 tax document PDF."

    # Fetch Case Messages Thread
    thread_res = await client.get(f"/api/v1/notifications/cases/{case_id}/messages", headers=headers)
    assert thread_res.status_code == 200
    thread = thread_res.json()
    assert len(thread) >= 1
    assert thread[0]["content"] == "Please send my 2025 W2 tax document PDF."
