from base.base_service import BaseService
from repositories.supply_repository import SupplyRepository

class SupplyService(BaseService):
    @property
    def repository(self) -> type[SupplyRepository]:
        return SupplyRepository()