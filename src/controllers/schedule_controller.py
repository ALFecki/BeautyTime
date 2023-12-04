from fastapi import APIRouter, Depends, Path
from services.schedule_service import ScheduleService
from schemas.schedule.schedule_schema_create import ScheduleSchemaCreate
from schemas.schedule.schedule_schema_update import ScheduleSchemaUpdate


router = APIRouter(prefix="/api/schedule", tags=["schedule"])


@router.get("/")
async def get_all_schedules(service=Depends(ScheduleService)):
    return await service.get_all()


@router.get("/{id}")
async def get_schedule_by_id(
    id: int = Path(example=1, description="ID искомой записи"),
    service=Depends(ScheduleService),
):
    return await service.get_by_id(id)


@router.post("/")
async def create_schedule(
    create_schema: ScheduleSchemaCreate, service=Depends(ScheduleService)
):
    return await service.create(create_schema)


@router.patch("/{id}")
async def update_schedule(
    update_schema: ScheduleSchemaUpdate,
    id: int = Path(example=1, description="ID обновляемой записи"),
    service=Depends(ScheduleService),
):
    return await service.update(id, update_schema)


@router.delete("/{id}")
async def delete_schedule(
    id: int = Path(example=1, description="ID удаляемой записи"),
    service=Depends(ScheduleService),
):
    return await service.delete(id)
