from fastapi import APIRouter, Depends, Path
from services.schedule_service import ScheduleService
from schemas.schedule.schedule_schema_create import ScheduleSchemaCreate
from schemas.schedule.schedule_schema_update import ScheduleSchemaUpdate
from schemas.user.user_schema import UserSchema
from services.auth_service import AuthService


router = APIRouter(prefix="/api/schedule", tags=["schedule"])


@router.get("/")
async def get_all_schedules(
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(ScheduleService),
):
    return await service.get_all(account=account)


@router.get("/{id}")
async def get_schedule_by_id(
    id: int = Path(example=1, description="ID искомой записи"),
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(ScheduleService),
):
    return await service.get_by_id(id, account=account)


@router.post("/")
async def create_schedule(
    create_schema: ScheduleSchemaCreate,
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(ScheduleService),
):
    return await service.create(create_schema, account=account)


@router.patch("/{id}")
async def update_schedule(
    update_schema: ScheduleSchemaUpdate,
    id: int = Path(example=1, description="ID обновляемой записи"),
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(ScheduleService),
):
    return await service.update(id, update_schema, account=account)


@router.delete("/{id}")
async def delete_schedule(
    id: int = Path(example=1, description="ID удаляемой записи"),
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(ScheduleService),
):
    return await service.delete(id, account=account)
