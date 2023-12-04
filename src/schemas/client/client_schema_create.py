from typing import Optional

from pydantic import BaseModel


class ClientSchemaCreate(BaseModel):
    user_id: int
    email: str
    first_name: str
    second_name: str
    surname: Optional[str]
    phone: str
