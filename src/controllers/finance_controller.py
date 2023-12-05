from fastapi import APIRouter, Depends, Path
from services.finance_service import FinanceService
from schemas.finance.finance_schema_create import FinanceSchemaCreate
from schemas.finance.finance_schema_update import FinanceSchemaUpdate
from schemas.user.user_schema import UserSchema
from services.auth_service import AuthService


router = APIRouter(prefix="/api/finance", tags=["finance"])


@router.get("/")
async def get_all_finances(
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(FinanceService),
):
    return await service.get_all(account=account)


@router.get("/{id}")
async def get_finance_by_id(
    id: int = Path(example=1, description="ID искомого финанса"),
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(FinanceService),
):
    return await service.get_by_id(id, account=account)


@router.post("/")
async def create_finance(
    create_schema: FinanceSchemaCreate,
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(FinanceService),
):
    return await service.create(create_schema, account=account)


@router.patch("/{id}")
async def update_finance(
    update_schema: FinanceSchemaUpdate,
    id: int = Path(example=1, description="ID обновляемого финанса"),
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(FinanceService),
):
    return await service.update(id, update_schema, account=account)


@router.delete("/{id}")
async def delete_finance(
    id: int = Path(example=1, description="ID удаляемого финанса"),
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(FinanceService),
):
    return await service.delete(id, account=account)
