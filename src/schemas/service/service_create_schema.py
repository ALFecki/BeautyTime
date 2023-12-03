from pydantic import BaseModel


class ServiceSchemaCreate(BaseModel):
    name: str
    alias: str
    description: str
    cost: float
