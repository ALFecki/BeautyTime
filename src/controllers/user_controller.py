

from fastapi import APIRouter, Depends
from services.user_service import UserService


router = APIRouter("/user")

@router.get("/")
async def get_all_user(
    service = Depends(UserService)
):
    return service.get_all()