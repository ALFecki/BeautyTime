from fastapi import APIRouter, Depends, Path
from services.user_service import UserService
from schemas.user.user_create_schema import UserSchemaCreate
from schemas.user.user_update_schema import UserSchemaUpdate
from schemas.user.user_schema import UserSchema
from services.auth_service import AuthService


router = APIRouter(prefix="/api/user", tags=["user"])


@router.get("/")
async def get_all_user(
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(UserService),
):
    return await service.get_all(account=account)


@router.get("/{id}")
async def get_user_by_id(
    id: int = Path(example=1, description="ID искомого юзера"),
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(UserService),
):
    return await service.get_by_id(id, account=account)


@router.post("/")
async def create_user(
    create_schema: UserSchemaCreate,
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(UserService),
):
    return await service.create(create_schema, account=account)


@router.patch("/{id}")
async def update_user(
    update_schema: UserSchemaUpdate,
    id: int = Path(example=1, description="ID обновляемого юзера"),
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(UserService),
):
    return await service.update(id, update_schema, account=account)


@router.delete("/{id}")
async def delete_user(
    id: int = Path(example=1, description="ID удаляемого юзера"),
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(UserService),
):
    return await service.delete(id, account=account)
