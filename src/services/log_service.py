from typing import Type
from src.base.base_service import BaseService
from src.repositories.log_repository import LogRepository

class LogService(BaseService):
    @property
    def repository(self) -> type[LogRepository]:
        return LogRepository