from typing import Any, Coroutine, Optional, Type
from base.base_service import AsyncSession, BaseService
from repositories.client_repository import ClientRepository
from base.base_repository import BaseRepo
from schemas.user.user_schema import UserSchema
from services.user_service import UserService


class ClientService(BaseService):
    @property
    def repository(self) -> type[ClientRepository]:
        return ClientRepository()
    

    def get_all(self, session: AsyncSession | None = None, account: UserSchema | None = None) -> Coroutine[Any, Any, Any]:
        user_service = UserService(session)

        return super().get_all(session, account)

