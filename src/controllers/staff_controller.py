from fastapi import APIRouter, Depends, Path
from services.staff_service import StaffService
from schemas.staff.staff_schema_create import StaffSchemaCreate
from schemas.staff.staff_schema_update import StaffSchemaUpdate
from schemas.user.user_schema import UserSchema
from services.auth_service import AuthService


router = APIRouter(prefix="/api/staff", tags=["staff"])


@router.get("/")
async def get_all_staffs(
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(StaffService),
):
    return await service.get_all(account=account)


@router.get("/{id}")
async def get_staff_by_id(
    id: int = Path(example=1, description="ID искомого клиента"),
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(StaffService),
):
    return await service.get_by_id(id, account=account)


@router.post("/")
async def create_staff(
    create_schema: StaffSchemaCreate,
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(StaffService),
):
    return await service.create(create_schema, account=account)


@router.patch("/{id}")
async def update_staff(
    update_schema: StaffSchemaUpdate,
    id: int = Path(example=1, description="ID обновляемого сотрудника"),
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(StaffService),
):
    return await service.update(id, update_schema, account=account)


@router.delete("/{id}")
async def delete_staff(
    id: int = Path(example=1, description="ID удаляемого сотрудника"),
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(StaffService),
):
    return await service.delete(id, account=account)
