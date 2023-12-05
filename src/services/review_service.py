from typing import Type

from fastapi import HTTPException, status
from base.base_service import AsyncSession, BaseService
from repositories.review_repository import ReviewRepository
from src.base.base_repository import BaseRepo
from src.schemas.user.user_schema import UserSchema
from src.services.admin_service import AdminService
from src.services.staff_service import StaffService
from src.models.employers.client_entity import Client
from src.services.client_service import ClientService


class ReviewService(BaseService):
    @property
    def repository(self) -> type[ReviewRepository]:
        return ReviewRepository()

    async def check_roles(self, user_id: int):
        admin_service = AdminService(self.async_session)
        staff_service = StaffService(self.async_session)
        client_service = ClientService(self.async_session)
        if (
            not await admin_service.check_admin_role(user_id)
            and not await staff_service.check_staff_role(user_id)
            and not client_service.check_client_role(user_id)
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Lack of access",
            )

    async def create(
        self,
        schema_create: BaseRepo.create_schema,
        session: AsyncSession | None = None,
        account: UserSchema | None = None,
    ):
        await self.check_roles(account.id)
        return await super().create(schema_create, session, account)

    async def update(
        self,
        id: int,
        schema_update: BaseRepo.update_schema,
        session: AsyncSession | None = None,
        account: UserSchema | None = None,
    ):
        await self.check_roles(account.id)
        return await super().update(id, schema_update, session, account)

    async def delete(
        self,
        id: int,
        session: AsyncSession | None = None,
        account: UserSchema | None = None,
    ):
        await self.check_roles(account.id)
        return await super().delete(id, session, account)
