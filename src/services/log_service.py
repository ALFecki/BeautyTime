from typing import Type
from base.base_service import BaseService
from repositories.log_repository import LogRepository

class LogService(BaseService):
    @property
    def repository(self) -> type[LogRepository]:
        return LogRepository()