from base.base_schema import BaseSchema
from schemas.user.user_schema import UserSchema
from typing import Optional

class ClientSchema(BaseSchema):
    user_id : int
    email: str
    first_name: str
    second_name: str
    surname: Optional[str] 
    phone: str
    user: UserSchema