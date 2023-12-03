from base.base_repository import BaseRepo
from schemas.product.product_schema import ProductSchema
from schemas.product.product_update_schema import ProductSchemaUpdate
from models.product_entity import Product
from schemas.product.product_create_schema import ProductSchemaCreate


class ProductRepository(BaseRepo):
    @property
    def model(self) -> type[Product]:
        return Product

    @property
    def schema(self) -> type[ProductSchema]:
        return ProductSchema

    @property
    def create_schema(self) -> type[ProductSchemaCreate]:
        return ProductSchemaCreate

    @property
    def update_schema(self) -> type[ProductSchemaUpdate]:
        return ProductSchemaUpdate
