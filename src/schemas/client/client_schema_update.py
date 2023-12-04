
from typing import Optional

from pydantic import BaseModel


class ClientSchemaUpdate(BaseModel):
    email: Optional[str]
    first_name: Optional[str]
    second_name: Optional[str]
    surname: Optional[str]
    phone: Optional[str]
