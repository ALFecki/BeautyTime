from base.base_schema import BaseSchema

class UserSchema(BaseSchema):
    id: int
    login: str
    password: str