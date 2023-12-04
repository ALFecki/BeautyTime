from typing import Type
from base.base_service import BaseService
from repositories.finance_repository import FinanceRepository

class FinanceService(BaseService):
    @property
    def repository(self) -> type[FinanceRepository]:
        return FinanceRepository()