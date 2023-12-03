from typing import Optional

from pydantic import BaseModel

class ServiceSchemaUpdate(BaseModel):
    name: Optional[str]
    alias: Optional[str]
    description: Optional[str]
    cost: Optional[float]
    