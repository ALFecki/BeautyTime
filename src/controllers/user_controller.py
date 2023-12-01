

from fastapi import APIRouter, Depends, Path
from services.user_service import UserService


router = APIRouter(prefix="/api/user", tags=["user"])

@router.get("/")
async def get_all_user(
    service = Depends(UserService)
):
    return await service.get_all()

@router.get("/{id}")
async def get_user_by_id(
    id: int = Path(example=1, description="ID искомого юзера"),
    service = Depends(UserService)
):
    return await service.get_by_id(id)