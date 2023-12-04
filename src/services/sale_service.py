from typing import Type
from base.base_service import BaseService
from repositories.sale_repository import SaleRepository

class SaleService(BaseService):

    @property
    def repository(self) -> type[SaleRepository]:
        return SaleRepository()