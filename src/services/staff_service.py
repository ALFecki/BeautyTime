from typing import Optional
from base.base_service import AsyncSession, BaseService
from repositories.staff_repository import StaffRepository


class StaffService(BaseService):
    @property
    def repository(self) -> type[StaffRepository]:
        return StaffRepository()
    

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

