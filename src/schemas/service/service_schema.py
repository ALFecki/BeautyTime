from base.base_schema import BaseSchema
from typing import Optional

class ServiceSchema(BaseSchema):
    name: str
    alias: str
    description: Optional[str]
    cost: float
    