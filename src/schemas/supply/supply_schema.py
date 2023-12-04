from typing import Optional
from base.base_schema import BaseSchema
from schemas.product.product_schema import ProductSchema


class SupplySchema(BaseSchema):
    product_id: int
    type: Optional[int]
    quantity: int
    sum: float
    product: ProductSchema
