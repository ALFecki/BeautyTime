from typing import Optional
from base.base_schema import BaseSchema
from schemas.user.user_schema import UserSchema


class StaffSchema(BaseSchema):
    user_id : int
    email: str
    first_name: str
    second_name: str
    position: Optional[str]
    phone: str
    user: UserSchema