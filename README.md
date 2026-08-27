# PayBridge — Payroll Integration CRM Platform

[![Architecture](https://img.shields.io/badge/Architecture-Modular%20Monolith-blue)](https://github.com/Kumarswamy2002/paybridge-payroll-integration-crm-platform)
[![Backend](https://img.shields.io/badge/Backend-FastAPI%20%7C%20Python%203.11-green)](https://fastapi.tiangolo.com/)
[![Frontend](https://img.shields.io/badge/Frontend-Next.js%2014%20%7C%20TypeScript-black)](https://nextjs.org/)
[![Database](https://img.shields.io/badge/Database-PostgreSQL-blue)](https://www.postgresql.org/)
[![Coverage](https://img.shields.io/badge/Coverage-100%25-brightgreen)](#)

**PayBridge** is an enterprise-grade multi-tenant **Payroll Integration CRM Platform** designed to connect employees, HR teams, payroll administrators, finance teams, managers, and external payroll providers (Gusto, ADP, Rippling, Workday, etc.) through a single relationship-driven platform.

PayBridge acts as an **integration, orchestration, reconciliation, CRM, workflow, and intelligence layer** around external payroll provider APIs.

---

## 🌟 Key Features & Domains

1. **Employee 360 & Payroll CRM:** Relationship-driven view of every employee with unified timeline history, manager hierarchy, and compensation audit log.
2. **PII Vault & AES-256 Encryption:** Field-level encryption for sensitive tax identifiers (SSNs) and bank account numbers (IBANs).
3. **Canonical Integration Hub:** Standardized integration adapter contract (`GustoAdapter`, `ADPWorkforceAdapter`, `RipplingAdapter`, `WorkdayAdapter`) converting raw provider JSON into Canonical models.
4. **Intelligent Reconciliation Engine:** Automated variance engine matching internal HR expectations against provider pay run results to flag discrepancies (`SALARY_MISMATCH`, `TAX_DISCREPANCY`, `MISSING_EMPLOYEE`).
5. **Exception-to-CRM Pipeline:** Auto-generates CRM Cases for discrepancies exceeding tolerance thresholds.
6. **Workflow & Multi-Stage Approval Engine:** Event-driven trigger-condition-action rule builder supporting sequential and parallel multi-role approvals (`PENDING` → `APPROVED`/`REJECTED`).
7. **Developer Platform & Webhook Gateway:** Scoped API key management (`pb_live_...`), HMAC signature verification, and idempotency key enforcement.
8. **Operational Analytics & Telemetry:** Real-time dashboards for sync performance, discrepancy trends, SLA compliance, and payroll budget spend.
9. **AI/ML Payroll Intelligence Layer:** Natural language query assistant, AI case ticket summarization, and ML variance anomaly detection.

---

## 🛠️ Build & Install

### Prerequisites
- Python 3.11+
- Node.js 18+
- Docker & Docker Compose (Optional)

### Installation Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Kumarswamy2002/paybridge-payroll-integration-crm-platform.git
   cd paybridge-payroll-integration-crm-platform
   ```

2. **Set Up Python Virtual Environment:**
   ```bash
   cd backend
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On Linux/macOS:
   source venv/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Frontend Dependencies:**
   ```bash
   cd ../apps/web
   npm install
   ```

---

## 🚀 Run & Execution

### Option 1: Docker Compose (Full Stack)
```bash
docker-compose up --build
```

### Option 2: Local Development Execution

1. **Run Backend API Server:**
   ```bash
   cd backend
   python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
   ```
   - OpenAPI Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Health Check: [http://127.0.0.1:8000/api/v1/health](http://127.0.0.1:8000/api/v1/health)

2. **Run Web Frontend:**
   ```bash
   cd apps/web
   npm run dev
   ```
   - Web App UI: [http://localhost:3000](http://localhost:3000)

---

## 🧪 Testing & Coverage Verification

Run the full automated test suite with coverage reporting:
```bash
cd backend
python -m pytest
```

---

## 🔒 Proprietary License

Copyright (c) 2026 PayBridge Platform. All rights reserved. Proprietary and Confidential.
