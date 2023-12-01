from typing import Type
from src.base.base_service import BaseRepository, BaseService
from src.repositories.user_repository import UserRepository

class UserService(BaseService):
    @property
    def repository(self) -> UserRepository:
        return UserRepository