from sqlalchemy import Row, text
from sqlalchemy.ext.asyncio import AsyncSession

from base.base_repository import BaseRepo
from models.employers.client_entity import Client
from schemas.client.client_schema import ClientSchema
from schemas.client.client_schema_create import ClientSchemaCreate
from schemas.client.client_schema_update import ClientSchemaUpdate
from schemas.user.user_schema import UserSchema
from base.base_service import AsyncSession
from utils.not_found_exception import NotFoundException
from schemas.client.client_schema_create_with_user import ClientSchemaCreateWithUser


class ClientRepository(BaseRepo):
    @property
    def model(self) -> type[Client]:
        return Client

    @property
    def schema(self) -> type[ClientSchema]:
        return ClientSchema

    @property
    def create_schema(self) -> type[ClientSchemaCreate]:
        return ClientSchemaCreate

    @property
    def update_schema(self) -> type[ClientSchemaUpdate]:
        return ClientSchemaUpdate

    async def create_with_user(
        self, session: AsyncSession, schema_create: ClientSchemaCreateWithUser
    ):
        statement = text(
            f"""CALL public.add_client(
                '{schema_create.login}',
                '{schema_create.password}',
                '{schema_create.email}',
                '{schema_create.first_name}',
                '{schema_create.second_name}',
                '{schema_create.surname}',
                '{schema_create.phone}'
                );"""
        )
        await session.execute(statement)

    async def create_response(self, row: Row):
        fields_dict = row._asdict()
        user = UserSchema.from_orm(fields_dict)
        user.id = fields_dict["user_id"]
        return self.schema(user=user, **fields_dict)

    async def get_all(self, session: AsyncSession):
        statement = text(
            f"""SELECT * FROM public.{self.model.__tablename__}
                         JOIN public.user ON client.user_id = public.user.id;"""
        )
        res = (await session.execute(statement)).fetchall()
        if res is None:
            raise NotFoundException(
                404,
                "Объект не найден",
                self.model.__name__ + " with current ID: " + str(id) + " was not found",
            )
        return [await self.create_response(obj) for obj in res]

    async def get_by_id(self, session: AsyncSession, id: int) -> UserSchema:
        statement = text(
            f"""SELECT * FROM public.{self.model.__tablename__}
            JOIN public.user ON {self.model.__tablename__}.user_id = public.user.id
            WHERE public.{self.model.__tablename__}.id = {id};"""
        )
        res = (await session.execute(statement)).fetchone()
        if res is None:
            raise NotFoundException(
                404,
                "Объект не найден",
                self.model.__name__ + " with current ID: " + str(id) + " was not found",
            )
        return await self.create_response(res)

    async def check_client_role(self, session: AsyncSession, user_id: int):
        return await self.get_by_user_id(session, user_id) is not None
