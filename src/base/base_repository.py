from abc import abstractmethod, ABC
from typing import Type, TypeVar
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text

from base.base_model import BaseEntity
from base.base_repository import CreateSchemaType
from base.base_schema import BaseSchema

ModelType = TypeVar("ModelType", bound=BaseEntity)
SchemaType = TypeVar("SchemaType", bound=BaseSchema)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)


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

    async def get_by_id(self, session: AsyncSession, id: int) -> ModelType | None:
        statement = text(f"""SELECT * FROM {self.model.__tablename__} WHERE id={id};""")
        return await session.execute(statement)

    async def get_all(self, session: AsyncSession) -> ModelType | None:
        statement = text(f"""SELECT * FROM {self.model.__tablename__};""")
        return await session.execute(statement)

    async def create(
        self, session: AsyncSession, schema_create: CreateSchemaType
    ) -> ModelType:
        fields_dict = schema_create.model_dump()
        statement = text(
            f"""INSERT INTO {self.model.__tablename__} ({(f'{key}, ' for key in fields_dict.keys())})
                         VALUES {(f'{value}, ' for value in fields_dict.values())};"""
        )
        return await session.execute(statement)
