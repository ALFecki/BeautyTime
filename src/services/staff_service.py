from src.base.base_service import BaseService
from src.repositories.staff_repository import StaffRepository


class StaffService(BaseService):
    @property
    def repository(self) -> type[StaffRepository]:
        return StaffRepository()

