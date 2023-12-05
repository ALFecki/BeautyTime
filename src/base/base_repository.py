from abc import abstractmethod, ABC
from typing import Type, TypeVar
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text

from base.base_model import BaseEntity
from base.base_schema import BaseSchema
from utils.not_found_exception import NotFoundException

ModelType = TypeVar("ModelType", bound=BaseEntity)
SchemaType = TypeVar("SchemaType", bound=BaseSchema)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class BaseRepo(ABC):
    @property
    @abstractmethod
    def model(self) -> Type[ModelType]:
        raise NotImplemented("Абстрактный метод не реализован")

    @property
    @abstractmethod
    def schema(self) -> Type[SchemaType]:
        raise NotImplemented("Абстрактный метод не реализован")

    @property
    @abstractmethod
    def create_schema(self) -> Type[CreateSchemaType]:
        raise NotImplemented("Абстрактный метод не реализован")

    @property
    @abstractmethod
    def update_schema(self) -> Type[UpdateSchemaType]:
        raise NotImplemented("Абстрактный метод не реализован")

    async def get_by_id(self, session: AsyncSession, id: int) -> SchemaType:
        statement = text(
            f"""SELECT * FROM public.{self.model.__tablename__} WHERE public.{self.model.__tablename__}.id = {id};"""
        )
        return self.schema.from_orm((await session.execute(statement)).fetchone())

    async def get_all(self, session: AsyncSession) -> [SchemaType]:
        statement = text(f"SELECT * FROM public.{self.model.__tablename__};")
        res = (await session.execute(statement)).fetchall()
        if res is None:
            raise NotFoundException(
                404,
                "Объект не найден",
                self.model.__name__ + " with current ID: " + str(id) + " was not found",
            )
        return [self.schema.from_orm(obj) for obj in res]

    async def create(self, session: AsyncSession, schema_create: CreateSchemaType):
        fields_dict = schema_create.model_dump()
        statement = text(
            f"""INSERT INTO public.{self.model.__tablename__} ({', '.join([key for key in fields_dict.keys()])})
                         VALUES {tuple(value for value in fields_dict.values())};"""
        )
        await session.execute(statement)

    async def update(
        self, session: AsyncSession, id: int, schemaUpdate: UpdateSchemaType
    ):
        fields_dict = schemaUpdate.model_dump()
        statement = text(
            f"""UPDATE public.{self.model.__tablename__}
                SET {', '.join([f"{key} = '{value}'" for key, value in fields_dict.items()])}
                WHERE public.{self.model.__tablename__}.id = {id};"""
        )
        await session.execute(statement)
        return await self.get_by_id(session, id)
    

    async def get_by_user_id(self, session: AsyncSession, user_id: int):
        statement = text(
            f"""SELECT * FROM public.{self.model.__tablename__}
            JOIN public.user ON {self.model.__tablename__}.user_id = public.user.id
            WHERE public.{self.model.__tablename__}.user_id = {user_id};"""
        )
        return (await session.execute(statement)).fetchone()

    async def delete(self, session: AsyncSession, id: int):
        statement = text(
            f"""DELETE FROM public.{self.model.__tablename__} WHERE public.{self.model.__tablename__}.id = {id}"""
        )
        await session.execute(statement)