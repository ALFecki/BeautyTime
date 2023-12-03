from pydantic import BaseModel
from typing import Optional

class UserSchemaUpdate(BaseModel):
    login: Optional[str]
    password: Optional[str]