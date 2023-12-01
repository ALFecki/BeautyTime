from abc import ABC, abstractmethod
from ast import TypeVar
from typing import Annotated, Optional, Type
from fastapi import Depends
from sqlalchemy.ext.asyncio import async_sessionmaker
from base.base_repository import BaseRepo

from db.session import get_session

AsyncSession = Annotated[async_sessionmaker, Depends(get_session)]

BaseRepository = TypeVar("BaseRepository", bound=BaseRepo)


class BaseService(ABC):
    @property
    @abstractmethod
    def repository(self) -> Type[BaseRepository]:
        ...

    def __init__(self, session: AsyncSession) -> None:
        self.async_session = session


    async def create(
        self,
        schema_create: BaseRepo.create_schema,
        session: Optional[AsyncSession] = None,
    ):
        if session:
            result = await self.get_by_id_without_activity(
                (await self._create(schema_create, session)).id, session
            )
        else:
            async with self.async_session.begin() as new_session:
                result = await self.get_by_id_without_activity(
                    (await self._create(schema_create, new_session)).id,
                    new_session,
                )
        return result


    async def _create(
        self,
        schema_create: BaseRepo.create_schema,
        session,
    ) -> BaseRepo.model:
        result = await self.repository.create(session, schema_create)
        return result
    

    async def get_by_id_without_activity(
        self, id: int, session=None
    ) -> BaseRepo.schema:
        """
        Получение данных по id
        :param id: id записи
        :param s: внешняя сессия
        :return:
        """
        if session:
            return await self._get_by_id_without_activity(session=session, id=id)
        else:
            async with self.async_session.begin() as session:
                return await self._get_by_id_without_activity(session=session, id=id)

    async def _get_by_id_without_activity(
        self, id: int, session=None
    ) -> BaseRepo.schema:
        return await self.repository.get_by_id(session=session, id=id)