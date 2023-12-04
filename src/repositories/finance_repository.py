from sqlalchemy import Row, text
from base.base_repository import BaseRepo
from base.base_service import AsyncSession
from models.finance_entity import Finance
from schemas.finance.finance_schema import FinanceSchema
from schemas.finance.finance_schema_create import FinanceSchemaCreate
from schemas.finance.finance_schema_update import FinanceSchemaUpdate
from utils.not_found_exception import NotFoundException
from repositories.sale_repository import SaleRepository
from repositories.schedule_repository import ScheduleRepository
from repositories.supply_repository import SupplyRepository


class FinanceRepository(BaseRepo):
    @property
    def model(self) -> type[Finance]:
        return Finance

    @property
    def schema(self) -> type[FinanceSchema]:
        return FinanceSchema

    @property
    def create_schema(self) -> type[FinanceSchemaCreate]:
        return FinanceSchemaCreate

    @property
    def update_schema(self) -> type[FinanceSchemaUpdate]:
        return FinanceSchemaUpdate

    async def create_response(self, row: Row, session: AsyncSession):
        fields_dict = row._asdict()
        if ("sale_id" in fields_dict and fields_dict["sale_id"] is not None):
            repo = SaleRepository()
            fields_dict["sale"] = await repo.get_by_id(session, fields_dict["sale_id"])
        elif ("schedule_id" in fields_dict and fields_dict["schedule_id"] is not None):
            repo = ScheduleRepository()
            fields_dict["schedule"] = await repo.get_by_id(session, fields_dict["schedule_id"])
        elif ("supply_id" in fields_dict and fields_dict["supply_id"] is not None):
            repo = SupplyRepository()
            fields_dict["supply"] = await repo.get_by_id(session, fields_dict["supply_id"])

        return self.schema(**fields_dict)

    async def get_all(self, session: AsyncSession):
        statement = text(
            f"""SELECT * FROM {self.model.__tablename__}"""
        )
        res = (await session.execute(statement)).fetchall()
        if res is None:
            raise NotFoundException(
                404,
                "Объект не найден",
                self.model.__name__ + " with current ID: " + str(id) + " was not found",
            )
        return [await self.create_response(obj, session) for obj in res]

    async def get_by_id(self, session: AsyncSession, id: int) -> FinanceSchema:
        statement = text(
            f"""SELECT * FROM {self.model.__tablename__}
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
