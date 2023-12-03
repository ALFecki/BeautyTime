from abc import ABC, abstractmethod
from typing import Annotated, Optional, Type, TypeVar
from fastapi import Depends
from sqlalchemy.ext.asyncio import async_sessionmaker
from base.base_repository import BaseRepo

from db.session import get_session
from base.base_model import Base

AsyncSession = Annotated[async_sessionmaker, Depends(get_session)]

BaseRepository = TypeVar("BaseRepository", bound=BaseRepo)


class BaseService(ABC):
    @property
    @abstractmethod
    def repository(self) -> Type[BaseRepository]:
        ...

    def __init__(self, session: AsyncSession) -> None:
        self.async_session = session

    async def get_by_id(
        self, id: int, session: Optional[AsyncSession] = None
    ) -> BaseRepo.schema:
        if session:
            return await self._get_by_id(session=session, id=id)
        else:
            async with self.async_session.begin() as session:
                return await self._get_by_id(session=session, id=id)

    async def _get_by_id(self, id: int, session=None) -> BaseRepo.schema:
        return await self.repository.get_by_id(session=session, id=id)

    async def get_all(self, session: Optional[AsyncSession] = None) -> BaseRepo.schema:
        if session:
            return await self._get_all(session=session)
        else:
            async with self.async_session.begin() as session:
                return await self._get_all(session=session)

    async def _get_all(self, session=None) -> [BaseRepo.schema]:
        return await self.repository.get_all(session=session)

    async def create(
        self,
        schema_create: BaseRepo.create_schema,
        session: Optional[AsyncSession] = None,
    ):
        if session:
            await self._create(schema_create, session)
        else:
            async with self.async_session.begin() as new_session:
                await self._create(schema_create, new_session)

    async def _create(
        self,
        schema_create: BaseRepo.create_schema,
        session: Optional[AsyncSession],
    ):
        await self.repository.create(session, schema_create)


    async def update(
        self,
        id: int,
        schema_update: BaseRepo.update_schema,
        session: Optional[AsyncSession] = None
    ):
        if session:
            return await self._update(session=session, id=id, schema_update=schema_update)
        else:
            async with self.async_session.begin() as session:
                return await self._update(session=session, id=id, schema_update=schema_update)
            

    async def _update(
        self,
        id: int,
        schema_update: BaseRepo.update_schema,
        session: Optional[AsyncSession]
    ):
        return await self.repository.update(session, id, schema_update)
        

    async def delete(self, id: int, session: Optional[AsyncSession] = None):
        if session:
            return await self._delete(session=session, id=id)
        else:
            async with self.async_session.begin() as session:
                return await self._delete(session=session, id=id)

    async def _delete(self, id: int, session: Optional[AsyncSession] = None):
        return await self.repository.delete(session=session, id=id)
