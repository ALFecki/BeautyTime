from base.base_service import BaseService
from repositories.service_repository import ServiceRepository


class ServiceService(BaseService):
    @property
    def repository(self) -> ServiceRepository:
        return ServiceRepository()