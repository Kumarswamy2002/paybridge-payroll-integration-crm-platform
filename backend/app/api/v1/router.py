from fastapi import APIRouter
from app.api.v1 import health, auth, tenants, organizations, employees, payroll, crm, integrations, reconciliation

api_router = APIRouter()

api_router.include_router(health.router, tags=["Health"])
api_router.include_router(auth.router, prefix="/auth", tags=["Auth"])
api_router.include_router(tenants.router, prefix="/tenants", tags=["Tenants"])
api_router.include_router(organizations.router, prefix="/orgs", tags=["Organizations"])
api_router.include_router(employees.router, prefix="/employees", tags=["Employees"])
api_router.include_router(payroll.router, prefix="/payroll", tags=["Payroll"])
api_router.include_router(crm.router, prefix="/crm", tags=["CRM & Cases"])
api_router.include_router(integrations.router, prefix="/integrations", tags=["Integration Platform"])
api_router.include_router(reconciliation.router, prefix="/reconciliation", tags=["Reconciliation & Exceptions"])
