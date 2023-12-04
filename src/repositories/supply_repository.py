from typing import Type

from sqlalchemy import Row, text
from base.base_repository import BaseRepo
from base.base_service import AsyncSession
from models.supply_entity import Supply
from schemas.product.product_schema import ProductSchema
from schemas.supply.supply_schema import SupplySchema
from schemas.supply.supply_schema_create import SupplySchemaCreate
from schemas.supply.supply_schema_update import SupplySchemaUpdate
from utils.not_found_exception import NotFoundException


class SupplyRepository(BaseRepo):
    @property
    def model(self) -> type[Supply]:
        return Supply

    @property
    def schema(self) -> type[SupplySchema]:
        return SupplySchema

    @property
    def create_schema(self) -> type[SupplySchemaCreate]:
        return SupplySchemaCreate

    @property
    def update_schema(self) -> type[SupplySchemaUpdate]:
        return SupplySchemaUpdate

    async def create_response(self, row: Row):
        fields_dict = row._asdict()

        product = ProductSchema.from_orm(fields_dict)
        product.id = fields_dict["product_id"]
        return self.schema(product=product, **fields_dict)

    async def get_all(self, session: AsyncSession):
        statement = text(
            f"""SELECT * FROM {self.model.__tablename__}
                JOIN product ON product.id = {self.model.__tablename__}.product_id"""
        )
        res = (await session.execute(statement)).fetchall()
        if res is None:
            raise NotFoundException(
                404,
                "Объект не найден",
                self.model.__name__ + " with current ID: " + str(id) + " was not found",
            )
        return [await self.create_response(obj) for obj in res]

    async def get_by_id(self, session: AsyncSession, id: int) -> SupplySchema:
        statement = text(
            f"""SELECT * FROM {self.model.__tablename__}
                JOIN product ON product.id = {self.model.__tablename__}.product_id
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
