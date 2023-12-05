from fastapi import APIRouter, Depends, Path
from schemas.client.client_schema_update import ClientSchemaUpdate
from services.client_service import ClientService
from schemas.client.client_schema_create import ClientSchemaCreate
from auth.middleware import oauth2_scheme

router = APIRouter(prefix="/api/client", tags=["client"])

@router.get("/")
async def get_all_clients(service=Depends(ClientService), token: str = Depends(oauth2_scheme)):
    return await service.get_all()


@router.get("/{id}")
async def get_client_by_id(
    id: int = Path(example=1, description="ID искомого клиента"),
    service=Depends(ClientService),
):
    return await service.get_by_id(id)


@router.post("/")
async def create_client(
    create_schema: ClientSchemaCreate, service=Depends(ClientService)
):
    return await service.create(create_schema)


@router.patch("/{id}")
async def update_client(
    update_schema: ClientSchemaUpdate,
    id: int = Path(example=1, description="ID обновляемого клиента"),
    service=Depends(ClientService),
):
    return await service.update(id, update_schema)


@router.delete("/{id}")
async def delete_client(
    id: int = Path(example=1, description="ID удаляемого клиента"),
    service=Depends(ClientService),
):
    return await service.delete(id)