from base.base_schema import BaseSchema
from schemas.user.user_schema import UserSchema

class AdminSchema(BaseSchema):
    user_id: int
    unique_id: str
    user: UserSchema