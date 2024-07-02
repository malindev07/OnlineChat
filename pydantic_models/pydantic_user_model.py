from dataclasses import field

from pydantic import BaseModel, Field
from pydantic.json_schema import SkipJsonSchema

from py_models.user_model import User


class UserPydantic(BaseModel):
    id: SkipJsonSchema[int] = None
    login: str
    password: str = Field(exclude = True)
    status: SkipJsonSchema[str] = None
    
    def convert_to_ReturnModel(self, user: User):
        if user is not None:
            self.login = user.login
            self.password = user.password
            self.id = user.id
            self.status = user.status
        
        return self


class UserSearchPydantic(UserPydantic):
    password: SkipJsonSchema[str] = None
    
    def convert_to_search_model(self, user: User):
        if user is not None:
            self.login = user.login
            self.id = user.id
            self.status = user.status
        
        return self
