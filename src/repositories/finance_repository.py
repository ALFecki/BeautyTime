from base.base_repository import BaseRepo
from src.models.finance_entity import Finance
from src.schemas.finance.finance_schema import FinanceSchema
from src.schemas.finance.finance_schema_create import FinanceSchemaCreate
from src.schemas.finance.finance_schema_update import FinanceSchemaUpdate


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

    async def create_response(self, row: Row):
        fields_dict = row._asdict()

        user = UserSchema.from_orm(fields_dict)
        user.id = fields_dict["user_id"]
        fields_dict["user"] = user.__dict__
        client = ClientSchema.from_orm(fields_dict)
        client.id = fields_dict["client_id"]

        product = ProductSchema.from_orm(fields_dict)
        product.id = fields_dict["product_id"]
        return self.schema(client=client, product=product, **fields_dict)

    async def get_all(self, session: AsyncSession):
        statement = text(
            f"""SELECT * FROM {self.model.__tablename__}
                JOIN product ON product.id = {self.model.__tablename__}.product_id
                JOIN client ON {self.model.__tablename__}.client_id = client.id
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

    async def get_by_id(self, session: AsyncSession, id: int) -> SchemaType:
        statement = text(
            f"""SELECT * FROM {self.model.__tablename__}
                JOIN product ON product.id = {self.model.__tablename__}.product_id
                JOIN client ON {self.model.__tablename__}.client_id = client.id
                JOIN public.user ON client.user_id = public.user.id
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
