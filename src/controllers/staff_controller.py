from fastapi import APIRouter, Depends, Path
from services.staff_service import StaffService
from schemas.staff.staff_schema_create import StaffSchemaCreate
from schemas.staff.staff_schema_update import StaffSchemaUpdate


router = APIRouter(prefix="/staff", tags=["staff"])


@router.get("/")
async def get_all_staffs(service=Depends(StaffService)):
    return await service.get_all()


@router.get("/{id}")
async def get_staff_by_id(
    id: int = Path(example=1, description="ID искомого клиента"),
    service=Depends(StaffService),
):
    return await service.get_by_id(id)


@router.post("/")
async def create_staff(create_schema: StaffSchemaCreate, service=Depends(StaffService)):
    return await service.create(create_schema)


@router.patch("/{id}")
async def update_staff(
    update_schema: StaffSchemaUpdate,
    id: int = Path(example=1, description="ID обновляемого сотрудника"),
    service=Depends(StaffService),
):
    return await service.update(id, update_schema)


@router.delete("/{id}")
async def delete_staff(
    id: int = Path(example=1, description="ID удаляемого сотрудника"),
    service=Depends(StaffService),
):
    return await service.delete(id)
