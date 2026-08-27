# PayBridge — Payroll Integration CRM Platform

[![Architecture](https://img.shields.io/badge/Architecture-Modular%20Monolith-blue)](https://github.com/Kumarswamy2002/paybridge-payroll-integration-crm-platform)
[![Backend](https://img.shields.io/badge/Backend-FastAPI%20%7C%20Python%203.11-green)](https://fastapi.tiangolo.com/)
[![Frontend](https://img.shields.io/badge/Frontend-Next.js%2014%20%7C%20TypeScript-black)](https://nextjs.org/)
[![Database](https://img.shields.io/badge/Database-PostgreSQL-blue)](https://www.postgresql.org/)

**PayBridge** is an enterprise-grade multi-tenant **Payroll Integration CRM Platform** designed to orchestrate, reconcile, synchronize, and provide CRM intelligence around external payroll providers (Gusto, ADP, Rippling, Workday, etc.).

PayBridge acts as an **integration, orchestration, reconciliation, CRM, workflow, and intelligence layer** around payroll systems.

The core business flow is:
`Employee → Payroll Profile → Payroll Provider → Integration → Synchronization → Validation → Reconciliation → Case Management → Resolution → Unified Timeline`

---

## 🌟 Key Features

1. **Employee 360 & Payroll CRM:** Relationship-driven view of every employee linking employment history, compensation changes, payroll profiles, tickets/cases, and provider sync records into a single timeline.
2. **Canonical Payroll Model:** Provider-independent internal data structures isolating external API schema differences.
3. **Provider Adapter Framework:** Modular adapter architecture for connecting Gusto, ADP, Rippling, and custom payroll systems.
4. **Intelligent Reconciliation:** Automated engine comparing internal HR records against external provider pay runs to instantly flag salary, tax, and deduction discrepancies.
5. **Exception-to-CRM Pipeline:** Automatic conversion of integration failures and pay run mismatches into structured, trackable CRM cases.
6. **Multi-Tenant & RBAC Architecture:** Strict tenant isolation with tenant context propagation and granular role-based access control (`SUPER_ADMIN`, `TENANT_ADMIN`, `HR_MANAGER`, `PAYROLL_ADMIN`, `EMPLOYEE`).
7. **Unified Timeline & Audit Trail:** Complete immutable audit history tracking every profile modification, sync event, and salary adjustment.

---

## 🏗️ Architecture Overview

```text
                               ┌──────────────────────────────────────────────┐
                               │             Next.js Frontend Apps            │
                               │   Web (HR/CRM)  | Admin  | Employee Portal  │
                               └──────────────────────┬───────────────────────┘
                                                      │ REST / WebSockets / OpenAPI
                               ┌──────────────────────▼───────────────────────┐
                               │           FastAPI API Gateway Layer          │
                               │       OAuth2 / JWT / Tenant / RBAC Middleware│
                               └──────────────────────┬───────────────────────┘
                                                      │
         ┌────────────────────────────────────────────┼────────────────────────────────────────────┐
         │                                            │                                            │
┌────────▼────────┐                         ┌─────────▼────────┐                         ┌─────────▼────────┐
│  Identity &     │                         │  Employee CRM &  │                         │   Integration    │
│  Tenants        │                         │  Payroll 360     │                         │   Platform       │
└────────┬────────┘                         └─────────┬────────┘                         └─────────┬────────┘
         │                                            │                                            │
         ├────────────────────────────────────────────┼────────────────────────────────────────────┤
         │                                            │                                            │
┌────────▼────────┐                         ┌─────────▼────────┐                         ┌─────────▼────────┐
│ Reconciliation  │                         │ Workflow Engine  │                         │ AI & Analytics   │
│ & Exception     │                         │ & Approvals      │                         │ Engine           │
└────────┬────────┘                         └─────────┬────────┘                         └─────────┬────────┘
         │                                            │                                            │
         └────────────────────────────────────────────┼────────────────────────────────────────────┘
                                                      │
                               ┌──────────────────────▼───────────────────────┐
                               │          Transactional Store                 │
                               │   PostgreSQL (Multi-tenant, Encrypted PII)  │
                               │   Redis (Cache / Distributed Locks)          │
                               │   Kafka / Event Bus (Outbox Streaming)       │
                               └──────────────────────────────────────────────┘
```

---

## 🛠️ Technology Stack

- **Backend:** Python 3.11+, FastAPI, Async SQLAlchemy 2.0, Pydantic v2, Alembic, Pytest
- **Frontend:** Next.js 14 (App Router), React 18, TypeScript, Tailwind CSS, Lucide Icons, TanStack Query
- **Database:** PostgreSQL, Redis
- **Security:** OAuth2 JWT bearer tokens, Passlib/Bcrypt, AES-256 GCM PII Encryption

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Node.js 18+ & npm
- PostgreSQL & Redis (or Docker)

### Backend Setup
```bash
cd backend
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt
pytest
uvicorn app.main:app --reload --port 8000
```

### Frontend Setup
```bash
cd apps/web
npm install
npm run dev
```

Visit the dashboard at `http://localhost:3000` and API docs at `http://localhost:8000/docs`.

---

## 🗺️ Multi-Phase Roadmap

- [x] **Phase 1 — Platform Foundation, Multi-Tenancy & Employee CRM**
- [ ] **Phase 2 — Payroll Profiles, Compensation & Case Management**
- [ ] **Phase 3 — Payroll Integration Hub & Canonical Engine**
- [ ] **Phase 4 — Intelligent Reconciliation & Exception Engine**
- [ ] **Phase 5 — Workflow Engine & Approval Automation**
- [ ] **Phase 6 — Communication Platform & Employee Portal**
- [ ] **Phase 7 — Public Developer Platform & Webhooks**
- [ ] **Phase 8 — Analytics Platform & Operational Intelligence**
- [ ] **Phase 9 — AI/ML Payroll Intelligence Layer**
- [ ] **Phase 10 — Production Hardening & CI/CD**

---

## 📄 License
Licensed under the Apache 2.0 License.
