from pydantic import BaseModel


class UserSchemaCreate(BaseModel):
    login: str
    password: str