from typing import List
from sqlalchemy import Row, text
from base.base_repository import BaseRepo
from base.base_service import AsyncSession
from models.employers.staff_entity import Staff
from schemas.staff.staff_schema import StaffSchema
from schemas.staff.staff_schema_create import StaffSchemaCreate
from schemas.staff.staff_schema_update import StaffSchemaUpdate
from schemas.user.user_schema import UserSchema
from utils.not_found_exception import NotFoundException


class StaffRepository(BaseRepo):
    @property
    def model(self) -> type[Staff]:
        return Staff

    @property
    def schema(self) -> type[StaffSchema]:
        return StaffSchema

    @property
    def create_schema(self) -> type[StaffSchemaCreate]:
        return StaffSchemaCreate

    @property
    def update_schema(self) -> type[StaffSchemaUpdate]:
        return StaffSchemaUpdate

    async def create_response(self, row: Row) -> StaffSchema:
        fields_dict = row._asdict()
        user = UserSchema.from_orm(fields_dict)
        return self.schema(user=user, **fields_dict)

    async def get_all(self, session: AsyncSession) -> List[StaffSchema]:
        statement = text(
            f"""SELECT * FROM public.{self.model.__tablename__}
                         JOIN public.user ON {self.model.__tablename__}.user_id = public.user.id;"""
        )
        res = (await session.execute(statement)).fetchall()
        if res is None:
            raise NotFoundException(
                404,
                "Объект не найден",
                self.model.__name__ + " with current ID: " + str(id) + " was not found",
            )
        return [await self.create_response(obj) for obj in res]

    async def get_by_id(self, session: AsyncSession, id: int) -> StaffSchema:
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

    async def check_staff_role(self, session: AsyncSession, user_id: int):
        return await self.get_by_user_id(session, user_id) is not None
