from fastapi import APIRouter, Depends, Path
from schemas.log.log_schema_update import LogSchemaUpdate

from services.log_service import LogService
from schemas.log.log_schema_create import LogSchemaCreate


router = APIRouter(prefix="/api/log", tags=["log"])


@router.get("/")
async def get_all_logs(service=Depends(LogService)):
    return await service.get_all()


@router.get("/{id}")
async def get_log_by_id(
    id: int = Path(example=1, description="ID искомого лога"),
    service=Depends(LogService),
):
    return await service.get_by_id(id)


@router.post("/")
async def create_log(
    create_schema: LogSchemaCreate, service=Depends(LogService)
):
    return await service.create(create_schema)


@router.patch("/{id}")
async def update_log(
    update_schema: LogSchemaUpdate,
    id: int = Path(example=1, description="ID обновляемого лога"),
    service=Depends(LogService),
):
    return await service.update(id, update_schema)


@router.delete("/{id}")
async def delete_log(
    id: int = Path(example=1, description="ID удаляемого лога"),
    service=Depends(LogService),
):
    return await service.delete(id)
