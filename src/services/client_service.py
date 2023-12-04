from typing import Type
from src.base.base_service import BaseService
from src.repositories.client_repository import ClientRepository


class ClientService(BaseService):
    @property
    def repository(self) -> type[ClientRepository]:
        return ClientRepository

        