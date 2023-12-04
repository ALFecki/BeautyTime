from base.base_service import BaseService
from repositories.staff_repository import StaffRepository


class StaffService(BaseService):
    @property
    def repository(self) -> type[StaffRepository]:
        return StaffRepository()

