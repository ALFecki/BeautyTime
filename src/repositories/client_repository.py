from typing import Type
from src.base.base_repository import BaseRepo
from src.models.employers.client_entity import Client
from src.schemas.client.client_schema import ClientSchema
from src.schemas.client.client_schema_create import ClientSchemaCreate
from src.schemas.client.client_schema_update import ClientSchemaUpdate

class ClientRepository(BaseRepo):
    @property
    def model(self) -> type[Client]:
        return Client

    @property
    def schema(self) -> type[ClientSchema]:
        return ClientSchema
    
    @property
    def create_schema(self) -> type[ClientSchemaCreate]:
        return ClientSchemaCreate
    
    @property
    def update_schema(self) -> type[ClientSchemaUpdate]:
        return ClientSchemaUpdate