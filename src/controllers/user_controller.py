from fastapi import APIRouter, Depends, Path
from services.user_service import UserService
from schemas.user.user_create_schema import UserSchemaCreate
from schemas.user.user_update_schema import UserSchemaUpdate


router = APIRouter(prefix="/api/user", tags=["user"])


@router.get("/")
async def get_all_user(service=Depends(UserService)):
    return await service.get_all()


@router.get("/{id}")
async def get_user_by_id(
    id: int = Path(example=1, description="ID искомого юзера"),
    service=Depends(UserService),
):
    return await service.get_by_id(id)


@router.post("/")
async def create_user(create_schema: UserSchemaCreate, service=Depends(UserService)):
    return await service.create(create_schema)


@router.patch("/{id}")
async def update_user(
    update_schema: UserSchemaUpdate,
    id: int = Path(example=1, description="ID обновляемого юзера"),
    service = Depends(UserService)
):
    return await service.update(id, update_schema)


@router.delete("/{id}")
async def delete_user(
    id: int = Path(example=1, description="ID удаляемого юзера"),
    service=Depends(UserService),
):
    return await service.delete(id)
