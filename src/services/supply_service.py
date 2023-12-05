from fastapi import HTTPException, status
from base.base_service import AsyncSession, BaseService
from repositories.supply_repository import SupplyRepository
from base.base_repository import BaseRepo
from schemas.user.user_schema import UserSchema
from services.admin_service import AdminService
from services.staff_service import StaffService

class SupplyService(BaseService):
    @property
    def repository(self) -> type[SupplyRepository]:
        return SupplyRepository()
    
    async def check_roles(self, user_id: int):
        admin_service = AdminService(self.async_session)
        staff_service = StaffService(self.async_session)
        if not await admin_service.check_admin_role(
            user_id
        ) and not await staff_service.check_staff_role(user_id):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Lack of access",
            )

    async def get_all(
        self, session: AsyncSession | None = None, account: UserSchema | None = None
    ):
        await self.check_roles(account.id)
        return await super().get_all(session, account)

    async def get_by_id(
        self,
        id: int,
        session: AsyncSession | None = None,
        account: UserSchema | None = None,
    ):
        await self.check_roles(account.id)
        return await super().get_by_id(id, session, account)

    async def create(
        self,
        schema_create: BaseRepo.create_schema,
        session: AsyncSession | None = None,
        account: UserSchema | None = None,
    ):
        await self.check_roles(account.id)
        return await super().create(schema_create, session, account)

    async def update(
        self,
        id: int,
        schema_update: BaseRepo.update_schema,
        session: AsyncSession | None = None,
        account: UserSchema | None = None,
    ):
        await self.check_roles(account.id)
        return await super().update(id, schema_update, session, account)

    async def delete(
        self,
        id: int,
        session: AsyncSession | None = None,
        account: UserSchema | None = None,
    ):
        await self.check_roles(account.id)
        return await super().delete(id, session, account)