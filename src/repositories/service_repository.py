from base.base_repository import BaseRepo
from schemas.service.service_update_schema import ServiceSchemaUpdate
from models.service_entity import Service
from schemas.service.service_schema import ServiceSchema
from schemas.service.service_create_schema import ServiceSchemaCreate


class ServiceRepository(BaseRepo):
    @property
    def model(self) -> type[Service]:
        return Service

    @property
    def schema(self) -> type[ServiceSchema]:
        return ServiceSchema

    @property
    def create_schema(self) -> type[ServiceSchemaCreate]:
        return ServiceSchemaCreate

    @property
    def update_schema(self) -> type[ServiceSchemaUpdate]:
        return ServiceSchemaUpdate