from typing import Type
from base.base_service import BaseService
from repositories.schedule_repository import ScheduleRepository

class ScheduleService(BaseService):
    @property
    def repository(self) -> type[ScheduleRepository]:
        return ScheduleRepository()