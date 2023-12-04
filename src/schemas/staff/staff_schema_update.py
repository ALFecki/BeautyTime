from typing import Optional
from src.base.base_schema import BaseSchema


class StaffSchemaUpdate(BaseSchema):    
    email: Optional[str]
    first_name: Optional[str]
    second_name: Optional[str]
    position: Optional[str]
    phone: Optional[str]