from base.base_service import BaseService
from repositories.product_repository import ProductRepository


class ProductService(BaseService):
    @property
    def repository(self) -> ProductRepository:
        return ProductRepository()