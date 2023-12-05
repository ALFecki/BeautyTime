from sqlalchemy import Row, text
from base.base_repository import BaseRepo
from base.base_service import AsyncSession
from models.employers.admin_entity import Admin
from schemas.admin.admin_schema import AdminSchema
from schemas.admin.admin_schema_create import AdminSchemaCreate
from schemas.admin.admin_schema_update import AdminSchemaUpdate
from schemas.user.user_schema import UserSchema
from utils.not_found_exception import NotFoundException


class AdminRepository(BaseRepo):
    @property
    def model(self) -> type[Admin]:
        return Admin

    @property
    def schema(self) -> type[AdminSchema]:
        return AdminSchema

    @property
    def create_schema(self) -> type[AdminSchemaCreate]:
        return AdminSchemaCreate

    @property
    def update_schema(self) -> type[AdminSchemaUpdate]:
        return AdminSchemaUpdate

    async def create_response(self, row: Row):
        fields_dict = row._asdict()
        user = UserSchema.from_orm(fields_dict)
        return self.schema(user=user, **fields_dict)

    async def get_all(self, session: AsyncSession):
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

    async def check_admin_role(self, session: AsyncSession, user_id: int):
        return await self.get_by_user_id(session, user_id) is not None
