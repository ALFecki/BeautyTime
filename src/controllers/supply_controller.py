from fastapi import APIRouter, Depends, Path
from services.supply_service import SupplyService
from schemas.supply.supply_schema_create import SupplySchemaCreate
from schemas.supply.supply_schema_update import SupplySchemaUpdate
from schemas.user.user_schema import UserSchema
from services.auth_service import AuthService


router = APIRouter(prefix="/api/supply", tags=["supply"])


@router.get("/")
async def get_all_supplies(
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(SupplyService),
):
    return await service.get_all()


@router.get("/{id}")
async def get_service_by_id(
    id: int = Path(example=1, description="ID искомой поставки"),
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(SupplyService),
):
    return await service.get_by_id(id)


@router.post("/")
async def create_service(
    create_schema: SupplySchemaCreate,
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(SupplyService),
):
    return await service.create(create_schema)


@router.patch("/{id}")
async def update_service(
    update_schema: SupplySchemaUpdate,
    id: int = Path(example=1, description="ID обновляемой поставки"),
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(SupplyService),
):
    return await service.update(id, update_schema)


@router.delete("/{id}")
async def delete_service(
    id: int = Path(example=1, description="ID удаляемой поставки"),
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(SupplyService),
):
    return await service.delete(id)
