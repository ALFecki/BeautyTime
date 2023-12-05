from typing import Type
from schemas.admin.admin_schema_create import AdminSchemaCreate
from base.base_service import BaseService
from repositories.admin_repository import AdminRepository

class AdminService(BaseService):
    @property
    def repository(self) -> type[AdminRepository]:
        return AdminRepository()