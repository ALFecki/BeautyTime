from typing import Type
from base.base_repository import BaseRepo
from models.employers.user_entity import User
from schemas.user.user_schema import UserSchema
from schemas.user.user_create_schema import UserSchemaCreate
from schemas.user.user_update_schema import UserSchemaUpdate


class UserRepository(BaseRepo):
    
    @property
    def model(self) -> type[User]:
        return User
    
    @property
    def schema(self) -> type[UserSchema]:
        return UserSchema
    
    @property
    def create_schema(self) -> type[UserSchemaCreate]:
        return UserSchemaCreate 
    
    @property
    def update_schema(self) -> type[UserSchemaUpdate]:
        return UserSchemaUpdate

