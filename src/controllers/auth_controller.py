from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from services.auth_service import AuthService


router = APIRouter(prefix="/api/token", tags=["token"])


@router.post("/")
async def login(login_data: OAuth2PasswordRequestForm = Depends(), service=Depends(AuthService)):
    return await service.login(login_data)
