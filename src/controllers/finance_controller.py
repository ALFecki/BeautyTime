from fastapi import APIRouter, Depends, Path
from services.finance_service import FinanceService
from schemas.finance.finance_schema_create import FinanceSchemaCreate
from schemas.finance.finance_schema_update import FinanceSchemaUpdate


router = APIRouter(prefix="/api/finance", tags=["finance"])


@router.get("/")
async def get_all_finances(service=Depends(FinanceService)):
    return await service.get_all()


@router.get("/{id}")
async def get_finance_by_id(
    id: int = Path(example=1, description="ID искомого финанса"),
    service=Depends(FinanceService),
):
    return await service.get_by_id(id)


@router.post("/")
async def create_finance(
    create_schema: FinanceSchemaCreate, service=Depends(FinanceService)
):
    return await service.create(create_schema)


@router.patch("/{id}")
async def update_finance(
    update_schema: FinanceSchemaUpdate,
    id: int = Path(example=1, description="ID обновляемого финанса"),
    service=Depends(FinanceService),
):
    return await service.update(id, update_schema)


@router.delete("/{id}")
async def delete_finance(
    id: int = Path(example=1, description="ID удаляемого финанса"),
    service=Depends(FinanceService),
):
    return await service.delete(id)
