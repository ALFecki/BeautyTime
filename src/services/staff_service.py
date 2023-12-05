from typing import Optional

from fastapi import HTTPException, status
from base.base_service import AsyncSession, BaseService
from repositories.staff_repository import StaffRepository
from base.base_repository import BaseRepo
from schemas.user.user_schema import UserSchema
from services.admin_service import AdminService


class StaffService(BaseService):
    @property
    def repository(self) -> type[StaffRepository]:
        return StaffRepository()

    async def check_roles(self, user_id: int):
        admin_service = AdminService(self.async_session)
        if not await admin_service.check_admin_role(user_id):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Lack of access",
            )

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

    async def check_staff_role(
        self,
        user_id: int,
        session: Optional[AsyncSession] = None,
    ):
        if session:
            return await self._check_staff_role(user_id, session=session)
        else:
            async with self.async_session.begin() as session:
                return await self._check_staff_role(user_id, session=session)

    async def _check_staff_role(self, user_id: int, session=None) -> bool:
        return await self.repository.check_staff_role(session=session, user_id=user_id)
