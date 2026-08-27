from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.schemas.auth import LoginRequest, Token, UserCreate, UserResponse
from app.services.auth_service import AuthService
from app.core.middleware import get_current_user, require_roles

router = APIRouter()

@router.post("/login", response_model=Token)
async def login(login_in: LoginRequest, db: AsyncSession = Depends(get_db)):
    return await AuthService.authenticate(db, login_in)

@router.post("/register", response_model=UserResponse)
async def register(user_in: UserCreate, db: AsyncSession = Depends(get_db)):
    return await AuthService.create_user(db, user_in)

@router.get("/me")
async def get_me(current_user: dict = Depends(get_current_user)):
    return current_user
