from fastapi import APIRouter, Depends, Path
from services.supply_service import SupplyService
from schemas.supply.supply_schema_create import SupplySchemaCreate
from schemas.supply.supply_schema_update import SupplySchemaUpdate


router = APIRouter(prefix="/api/supply", tags=["supply"])


@router.get("/")
async def get_all_supplies(service=Depends(SupplyService)):
    return await service.get_all()


@router.get("/{id}")
async def get_service_by_id(
    id: int = Path(example=1, description="ID искомой поставки"),
    service=Depends(SupplyService),
):
    return await service.get_by_id(id)


@router.post("/")
async def create_service(
    create_schema: SupplySchemaCreate, service=Depends(SupplyService)
):
    return await service.create(create_schema)


@router.patch("/{id}")
async def update_service(
    update_schema: SupplySchemaUpdate,
    id: int = Path(example=1, description="ID обновляемой поставки"),
    service=Depends(SupplyService),
):
    return await service.update(id, update_schema)


@router.delete("/{id}")
async def delete_service(
    id: int = Path(example=1, description="ID удаляемой поставки"),
    service=Depends(SupplyService),
):
    return await service.delete(id)
