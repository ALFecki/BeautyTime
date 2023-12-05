from typing import Any, Coroutine, Optional, Type

from fastapi import HTTPException, status
from base.base_service import AsyncSession, BaseService
from repositories.client_repository import ClientRepository
from base.base_repository import BaseRepo
from schemas.user.user_schema import UserSchema
from services.user_service import UserService
from services.admin_service import AdminService
from services.staff_service import StaffService


class ClientService(BaseService):
    @property
    def repository(self) -> type[ClientRepository]:
        return ClientRepository()

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
    ) -> Coroutine[Any, Any, Any]:
        await self.check_roles(account.id)
        return await super().get_all(session, account)

    async def get_by_id(
        self,
        id: int,
        session: AsyncSession | None = None,
        account: UserSchema | None = None,
    ) -> Coroutine[Any, Any, Any]:
        await self.check_roles(account.id)
        return await super().get_by_id(id, session, account)

    async def update(
        self,
        id: int,
        schema_update: BaseRepo.update_schema,
        session: AsyncSession | None = None,
        account: UserSchema | None = None,
    ):
        await self.check_roles(account.id)
        if not await self.check_client_role(account.id):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Lack of access",
            )
        return await super().update(id, schema_update, session, account)

    async def delete(
        self,
        id: int,
        session: AsyncSession | None = None,
        account: UserSchema | None = None,
    ):
        await self.check_roles(account.id)
        return await super().delete(id, session, account)

    async def check_client_role(
        self,
        user_id: int,
        session: Optional[AsyncSession] = None,
    ):
        if session:
            return await self._check_client_role(user_id, session=session)
        else:
            async with self.async_session.begin() as session:
                return await self._check_client_role(user_id, session=session)

    async def _check_client_role(self, user_id: int, session=None) -> bool:
        return await self.repository.check_client_role(session=session, user_id=user_id)
