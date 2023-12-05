from fastapi import APIRouter, Depends, Path
from schemas.client.client_schema_update import ClientSchemaUpdate
from services.client_service import ClientService
from schemas.client.client_schema_create import ClientSchemaCreate
from auth.middleware import oauth2_scheme
from services.auth_service import AuthService
from schemas.user.user_schema import UserSchema

router = APIRouter(prefix="/api/client", tags=["client"])


@router.get("/")
async def get_all_clients(
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(ClientService),
):
    return await service.get_all(account=account)


@router.get("/{id}")
async def get_client_by_id(
    id: int = Path(example=1, description="ID искомого клиента"),
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(ClientService),
):
    return await service.get_by_id(id, account=account)


@router.post("/")
async def create_client(
    create_schema: ClientSchemaCreate, service=Depends(ClientService)
):
    return await service.create(create_schema)


@router.patch("/{id}")
async def update_client(
    update_schema: ClientSchemaUpdate,
    id: int = Path(example=1, description="ID обновляемого клиента"),
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(ClientService),
):
    return await service.update(id, update_schema, account=account)


@router.delete("/{id}")
async def delete_client(
    id: int = Path(example=1, description="ID удаляемого клиента"),
    account: UserSchema = Depends(AuthService.get_current_user),
    service=Depends(ClientService),
):
    return await service.delete(id, account=account)
