from typing import Optional
from base.base_schema import BaseSchema


class StaffSchemaCreate(BaseSchema):
    user_id : int
    email: str
    first_name: str
    second_name: str
    position: Optional[str]
    phone: str