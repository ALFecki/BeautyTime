from fastapi import APIRouter, Depends, Path
from services.service_service import ServiceService
from schemas.service.service_create_schema import ServiceSchemaCreate
from schemas.service.service_update_schema import ServiceSchemaUpdate


router = APIRouter(prefix="/api/service", tags=["service"])


@router.get("/")
async def get_all_services(service=Depends(ServiceService)):
    return await service.get_all()


@router.get("/{id}")
async def get_service_by_id(
    id: int = Path(example=1, description="ID искомой услуги"),
    service=Depends(ServiceService),
):
    return await service.get_by_id(id)


@router.post("/")
async def create_service(
    create_schema: ServiceSchemaCreate, service=Depends(ServiceService)
):
    return await service.create(create_schema)


@router.patch("/{id}")
async def update_service(
    update_schema: ServiceSchemaUpdate,
    id: int = Path(example=1, description="ID обновляемой услуги"),
    service=Depends(ServiceService),
):
    return await service.update(id, update_schema)


@router.delete("/{id}")
async def delete_service(
    id: int = Path(example=1, description="ID удаляемой услуги"),
    service=Depends(ServiceService),
):
    return await service.delete(id)
