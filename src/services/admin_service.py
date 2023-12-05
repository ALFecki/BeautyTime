from typing import Optional, Type

from fastapi import HTTPException, status
from schemas.admin.admin_schema_create import AdminSchemaCreate
from base.base_service import AsyncSession, BaseService
from repositories.admin_repository import AdminRepository
from schemas.user.user_schema import UserSchema
from src.base.base_repository import BaseRepo


class AdminService(BaseService):
    @property
    def repository(self) -> type[AdminRepository]:
        return AdminRepository()
    
    async def check_roles(self, user_id: int):
        if not await self.check_admin_role(user_id):
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



    async def check_admin_role(
        self,
        user_id: int,
        session: Optional[AsyncSession] = None,
    ):
        if session:
            return await self._check_admin_role(user_id, session=session)
        else:
            async with self.async_session.begin() as session:
                return await self._check_admin_role(user_id, session=session)

    async def _check_admin_role(self, user_id: int, session=None) -> bool:
        return await self.repository.check_admin_role(session=session, user_id=user_id)
