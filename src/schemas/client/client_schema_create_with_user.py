from typing import Optional
from pydantic import BaseModel


class ClientSchemaCreateWithUser(BaseModel):
    login: str
    password: str
    email: str
    first_name: str
    second_name: str
    surname: Optional[str]
    phone: str
