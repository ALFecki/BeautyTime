from typing import Optional, Type
from base.base_service import AsyncSession, BaseRepository, BaseService
from repositories.user_repository import UserRepository

class UserService(BaseService):
    @property
    def repository(self) -> UserRepository:
        return UserRepository()
    
    async def get_by_login(
        self, login: str, session: Optional[AsyncSession] = None
    ):
        if session:
            return await self._get_by_login(session=session, login=login)
        else:
            async with self.async_session.begin() as session:
                return await self._get_by_login(session=session, login=login)
            

    async def _get_by_login(
            self, login: str, session: AsyncSession
    ):
        return await self.repository.get_by_login(session, login)