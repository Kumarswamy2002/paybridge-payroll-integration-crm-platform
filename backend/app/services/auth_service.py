from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException, status
from app.models.user import User
from app.models.tenant import Tenant
from app.schemas.auth import UserCreate, LoginRequest
from app.core.security import get_password_hash, verify_password, create_access_token, create_refresh_token

class AuthService:
    @staticmethod
    async def create_user(db: AsyncSession, user_in: UserCreate) -> User:
        # Check existing user
        result = await db.execute(
            select(User).where(User.email == user_in.email, User.tenant_id == user_in.tenant_id)
        )
        if result.scalars().first():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User with this email already exists in this tenant"
            )

        hashed_pwd = get_password_hash(user_in.password)
        user = User(
            tenant_id=user_in.tenant_id,
            email=user_in.email,
            hashed_password=hashed_pwd,
            full_name=user_in.full_name,
            role=user_in.role,
            is_active=True
        )
        db.add(user)
        await db.commit()
        await db.refresh(user)
        return user

    @staticmethod
    async def authenticate(db: AsyncSession, login_in: LoginRequest) -> dict:
        # Find tenant first
        tenant_result = await db.execute(
            select(Tenant).where(Tenant.slug == login_in.tenant_slug)
        )
        tenant = tenant_result.scalars().first()
        if not tenant:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Tenant not found"
            )

        # Find user in tenant
        user_result = await db.execute(
            select(User).where(User.email == login_in.email, User.tenant_id == tenant.id)
        )
        user = user_result.scalars().first()
        if not user or not verify_password(login_in.password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password"
            )

        access_token = create_access_token(user.id, user.tenant_id, user.role)
        refresh_token = create_refresh_token(user.id, user.tenant_id)

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
            "user_id": user.id,
            "tenant_id": user.tenant_id,
            "role": user.role,
        }
