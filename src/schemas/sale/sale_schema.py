from datetime import datetime
from base.base_schema import BaseSchema
from schemas.client.client_schema import ClientSchema
from schemas.product.product_schema import ProductSchema

class SaleSchema(BaseSchema):
    client_id: int
    product_id: int
    quantity: int
    sale_date: datetime
    client: ClientSchema
    product: ProductSchema