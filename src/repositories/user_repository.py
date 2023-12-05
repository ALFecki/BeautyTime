from typing import Type

from sqlalchemy import text
from base.base_repository import BaseRepo
from models.employers.user_entity import User
from schemas.user.user_schema import UserSchema
from schemas.user.user_create_schema import UserSchemaCreate
from schemas.user.user_update_schema import UserSchemaUpdate
from base.base_service import AsyncSession
from utils.not_found_exception import NotFoundException


class UserRepository(BaseRepo):
    @property
    def model(self) -> type[User]:
        return User

    @property
    def schema(self) -> type[UserSchema]:
        return UserSchema

    @property
    def create_schema(self) -> type[UserSchemaCreate]:
        return UserSchemaCreate

    @property
    def update_schema(self) -> type[UserSchemaUpdate]:
        return UserSchemaUpdate

    async def get_by_login(self, session: AsyncSession, login: str):
        statement = text(
            f"SELECT * FROM public.user WHERE public.user.login = '{login}';"
        )
        res = await session.execute(statement)
        if res is None:
            raise NotFoundException(
                404,
                "Объект не найден",
                self.model.__name__ + " with current ID: " + str(id) + " was not found",
            )

        return UserSchema.from_orm(res.fetchone())
