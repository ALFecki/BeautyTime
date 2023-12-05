from typing import Optional, Type
from schemas.admin.admin_schema_create import AdminSchemaCreate
from base.base_service import AsyncSession, BaseService
from repositories.admin_repository import AdminRepository
from schemas.user.user_schema import UserSchema


class AdminService(BaseService):
    @property
    def repository(self) -> type[AdminRepository]:
        return AdminRepository()

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
