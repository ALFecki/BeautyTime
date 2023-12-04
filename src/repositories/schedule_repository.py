from sqlalchemy import Row, text
from base.base_repository import BaseRepo
from base.base_service import AsyncSession
from models.schedule_entity import Schedule
from schemas.client.client_schema import ClientSchema
from schemas.schedule.schedule_schema import ScheduleSchema
from schemas.schedule.schedule_schema_create import ScheduleSchemaCreate
from schemas.schedule.schedule_schema_update import ScheduleSchemaUpdate
from schemas.staff.staff_schema import StaffSchema
from schemas.user.user_schema import UserSchema
from utils.not_found_exception import NotFoundException
from schemas.service.service_schema import ServiceSchema


class ScheduleRepository(BaseRepo):
    @property
    def model(self) -> type[Schedule]:
        return Schedule

    @property
    def schema(self) -> type[ScheduleSchema]:
        return ScheduleSchema

    @property
    def create_schema(self) -> type[ScheduleSchemaCreate]:
        return ScheduleSchemaCreate

    @property
    def update_schema(self) -> type[ScheduleSchemaUpdate]:
        return ScheduleSchemaUpdate

    async def create_response(self, row: Row, session: AsyncSession):
        fields_dict = row._asdict()
        statement = text(
            f"""SELECT * FROM client 
                JOIN public.user ON public.user.id = client.user_id
                WHERE client.id = {fields_dict['client_id']};"""
        )

        res = (await session.execute(statement)).fetchone()._asdict()
        
        user = UserSchema.from_orm(res)
        user.id = res["user_id"]
        res["user"] = user.__dict__
        
        client = ClientSchema.from_orm(res)
        client.id = fields_dict["client_id"]

        statement = text(
            f"""SELECT * FROM staff 
                JOIN public.user ON public.user.id = staff.user_id
                WHERE staff.id = {fields_dict['staff_id']};"""
        )

        res = (await session.execute(statement)).fetchone()._asdict()

        user = UserSchema.from_orm(res)
        user.id = res["user_id"]
        res["user"] = user.__dict__
        
        staff = StaffSchema.from_orm(res)
        client.id = fields_dict["staff_id"]

        service = ServiceSchema.from_orm(fields_dict)
        service.id = fields_dict["service_id"]
        return self.schema(client=client, staff=staff, service=service, **fields_dict)

    async def get_all(self, session: AsyncSession):
        statement = text(
            f"""SELECT * FROM {self.model.__tablename__}
                JOIN service ON service.id = {self.model.__tablename__}.service_id;"""
        )
        res = (await session.execute(statement)).fetchall()
        if res is None:
            raise NotFoundException(
                404,
                "Объект не найден",
                self.model.__name__ + " with current ID: " + str(id) + " was not found",
            )
        return [await self.create_response(obj, session) for obj in res]

    async def get_by_id(self, session: AsyncSession, id: int) -> ScheduleSchema:
        statement = text(
            f"""SELECT * FROM {self.model.__tablename__}
                JOIN service ON service.id = {self.model.__tablename__}.service_id
                WHERE public.{self.model.__tablename__}.id = {id};"""
        )
        res = (await session.execute(statement)).fetchone()
        if res is None:
            raise NotFoundException(
                404,
                "Объект не найден",
                self.model.__name__ + " with current ID: " + str(id) + " was not found",
            )
        return await self.create_response(res, session)
