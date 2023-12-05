from sqlalchemy import Row, text
from src.base.base_repository import BaseRepo
from src.base.base_service import AsyncSession
from src.models.review_entity import Review
from src.repositories.schedule_repository import ScheduleRepository
from src.schemas.reviews.review_schema import ReviewSchema
from src.schemas.reviews.review_schema_create import ReviewSchemaCreate
from src.schemas.reviews.review_schema_update import ReviewSchemaUpdate
from src.repositories.client_repository import ClientRepository
from src.utils.not_found_exception import NotFoundException


class ReviewRepository(BaseRepo):
    @property
    def model(self) -> type[Review]:
        return Review

    @property
    def schema(self) -> type[ReviewSchema]:
        return ReviewSchema

    @property
    def create_schema(self) -> type[ReviewSchemaCreate]:
        return ReviewSchemaCreate

    @property
    def update_schema(self) -> type[ReviewSchemaUpdate]:
        return ReviewSchemaUpdate

    async def create_response(self, row: Row, session: AsyncSession):
        fields_dict = row._asdict()

        repo = ScheduleRepository()
        fields_dict["schedule"] = await repo.get_by_id(
            session, fields_dict["schedule_id"]
        )

        repo = ClientRepository()
        fields_dict["client"] = await repo.get_by_id(session, fields_dict["client_id"])

        return self.schema(**fields_dict)

    async def get_all(self, session: AsyncSession):
        statement = text(f"""SELECT * FROM {self.model.__tablename__}""")
        res = (await session.execute(statement)).fetchall()
        if res is None:
            raise NotFoundException(
                404,
                "Объект не найден",
                self.model.__name__ + " with current ID: " + str(id) + " was not found",
            )
        return [await self.create_response(obj, session) for obj in res]

    async def get_by_id(self, session: AsyncSession, id: int) -> ReviewSchema:
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
