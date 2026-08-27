from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import func
from app.models.employee import Employee, EmploymentHistory, EmployeeRelationship
from app.models.org import Department, JobPosition
from app.models.payroll import PayrollProfile, Compensation
from app.models.crm import CRMCase, UnifiedTimelineEvent
from app.schemas.employee import EmployeeCreate, EmployeeUpdate, Employee360Response

class EmployeeService:
    @staticmethod
    async def create_employee(db: AsyncSession, tenant_id: str, emp_in: EmployeeCreate) -> Employee:
        employee = Employee(
            tenant_id=tenant_id,
            employee_code=emp_in.employee_code,
            first_name=emp_in.first_name,
            last_name=emp_in.last_name,
            email=emp_in.email,
            phone=emp_in.phone,
            department_id=emp_in.department_id,
            job_position_id=emp_in.job_position_id,
            manager_id=emp_in.manager_id,
            employment_type=emp_in.employment_type,
            status=emp_in.status,
            date_of_joining=emp_in.date_of_joining,
            work_location=emp_in.work_location
        )
        db.add(employee)
        await db.commit()
        await db.refresh(employee)

        # Log timeline event
        timeline_event = UnifiedTimelineEvent(
            tenant_id=tenant_id,
            employee_id=employee.id,
            event_type="EMPLOYEE_CREATED",
            summary=f"Employee Profile created for {employee.first_name} {employee.last_name}",
            details={"employee_code": employee.employee_code, "email": employee.email},
            actor_name="HR Administrator"
        )
        db.add(timeline_event)
        await db.commit()

        return employee

    @staticmethod
    async def list_employees(
        db: AsyncSession, 
        tenant_id: str, 
        department_id: Optional[str] = None, 
        status: Optional[str] = None
    ) -> List[Employee]:
        query = select(Employee).where(Employee.tenant_id == tenant_id)
        if department_id:
            query = query.where(Employee.department_id == department_id)
        if status:
            query = query.where(Employee.status == status)
        
        result = await db.execute(query)
        return result.scalars().all()

    @staticmethod
    async def get_employee_by_id(db: AsyncSession, tenant_id: str, employee_id: str) -> Optional[Employee]:
        result = await db.execute(
            select(Employee).where(Employee.id == employee_id, Employee.tenant_id == tenant_id)
        )
        return result.scalars().first()

    @staticmethod
    async def get_employee_360(db: AsyncSession, tenant_id: str, employee_id: str) -> Optional[Employee360Response]:
        employee = await EmployeeService.get_employee_by_id(db, tenant_id, employee_id)
        if not employee:
            return None

        # Fetch department
        dept_name = None
        if employee.department_id:
            dept_res = await db.execute(select(Department).where(Department.id == employee.department_id))
            dept = dept_res.scalars().first()
            if dept:
                dept_name = dept.name

        # Fetch position
        pos_title = None
        if employee.job_position_id:
            pos_res = await db.execute(select(JobPosition).where(JobPosition.id == employee.job_position_id))
            pos = pos_res.scalars().first()
            if pos:
                pos_title = pos.title

        # Fetch manager
        mgr_name = None
        if employee.manager_id:
            mgr_res = await db.execute(select(Employee).where(Employee.id == employee.manager_id))
            mgr = mgr_res.scalars().first()
            if mgr:
                mgr_name = f"{mgr.first_name} {mgr.last_name}"

        # Fetch payroll profile
        payroll_provider = None
        sync_status = None
        payroll_res = await db.execute(select(PayrollProfile).where(PayrollProfile.employee_id == employee_id))
        payroll = payroll_res.scalars().first()
        if payroll:
            payroll_provider = payroll.payroll_provider
            sync_status = payroll.sync_status

        # Fetch compensation
        base_salary = None
        comp_res = await db.execute(
            select(Compensation).where(Compensation.employee_id == employee_id, Compensation.status == "ACTIVE")
        )
        comp = comp_res.scalars().first()
        if comp:
            base_salary = comp.base_salary

        # Fetch cases count
        cases_count_res = await db.execute(
            select(func.count(CRMCase.id)).where(CRMCase.employee_id == employee_id, CRMCase.status != "CLOSED")
        )
        cases_count = cases_count_res.scalar() or 0

        return Employee360Response(
            employee=employee,
            department_name=dept_name,
            position_title=pos_title,
            manager_name=mgr_name,
            payroll_provider=payroll_provider,
            sync_status=sync_status,
            base_salary=base_salary,
            open_cases_count=cases_count
        )
