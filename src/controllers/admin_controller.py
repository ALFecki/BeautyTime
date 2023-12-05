from fastapi import APIRouter, Depends, Path
from schemas.admin.admin_schema_create import AdminSchemaCreate
from schemas.user.user_schema import UserSchema
from services.admin_service import AdminService
from services.auth_service import AuthService
from schemas.admin.admin_schema_update import AdminSchemaUpdate


router = APIRouter(prefix="/api/admin", tags=["admin"])


@router.get("/")
async def get_all_admins(
    service=Depends(AdminService),
    account: UserSchema = Depends(AuthService.get_current_user),
):
    return await service.get_all()


@router.get("/{id}")
async def get_admin_by_id(
    id: int = Path(example=1, description="ID искомого админа"),
    service=Depends(AdminService),
):
    return await service.get_by_id(id)


@router.post("/")
async def create_admin(create_schema: AdminSchemaCreate, service=Depends(AdminService)):
    return await service.create(create_schema)


@router.patch("/{id}")
async def update_admin(
    update_schema: AdminSchemaUpdate,
    id: int = Path(example=1, description="ID обновляемого админа"),
    service=Depends(AdminService),
):
    return await service.update(id, update_schema)


@router.delete("/{id}")
async def delete_admin(
    id: int = Path(example=1, description="ID удаляемого админа"),
    service=Depends(AdminService),
):
    return await service.delete(id)
