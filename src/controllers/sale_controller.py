from fastapi import APIRouter, Depends, Path
from services.sale_service import SaleService
from schemas.sale.sale_schema_create import SaleSchemaCreate
from schemas.sale.sale_schema_update import SaleSchemaUpdate
from schemas.user.user_schema import UserSchema
from services.auth_service import AuthService


router = APIRouter(prefix="/api/sale", tags=["sale"])


@router.get("/")
async def get_all_sales(
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(SaleService),
):
    return await service.get_all()


@router.get("/{id}")
async def get_sale_by_id(
    id: int = Path(example=1, description="ID искомой продажи"),
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(SaleService),
):
    return await service.get_by_id(id)


@router.post("/")
async def create_sale(
    create_schema: SaleSchemaCreate,
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(SaleService),
):
    return await service.create(create_schema)


@router.patch("/{id}")
async def update_sale(
    update_schema: SaleSchemaUpdate,
    id: int = Path(example=1, description="ID обновляемой продажи"),
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(SaleService),
):
    return await service.update(id, update_schema)


@router.delete("/{id}")
async def delete_sale(
    id: int = Path(example=1, description="ID удаляемой продажи"),
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(SaleService),
):
    return await service.delete(id)
