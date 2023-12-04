from typing import Type
from base.base_service import BaseService
from repositories.client_repository import ClientRepository


class ClientService(BaseService):
    @property
    def repository(self) -> type[ClientRepository]:
        return ClientRepository()

