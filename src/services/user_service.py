from typing import Type
from base.base_service import BaseRepository, BaseService
from repositories.user_repository import UserRepository

class UserService(BaseService):
    @property
    def repository(self) -> UserRepository:
        return UserRepository