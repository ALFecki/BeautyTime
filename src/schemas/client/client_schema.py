from src.base.base_schema import BaseSchema
from src.schemas.user.user_schema import UserSchema

class ClientSchema(BaseSchema):
    user_id : int
    email: str
    first_name: str
    second_name: str
    surname: str 
    phone: str
    user: UserSchema