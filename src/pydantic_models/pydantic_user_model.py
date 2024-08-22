from pydantic import BaseModel
from pydantic.json_schema import SkipJsonSchema

from src.py_models.user_model import User


class UserPydantic(BaseModel):
    id: SkipJsonSchema[int] = None
    login: str
    password: str
    status: SkipJsonSchema[str] = None
    chats_id: SkipJsonSchema[list[int]] = None
    old_logins: SkipJsonSchema[list[str]] = None
    
    async def convert_to_return_model(self, user: User):
        if user is not None:
            self.login = user.login
            self.password = user.password
            self.id = user.id
            self.status = user.status
            self.chats_id = user.chats_id
            self.old_logins = user.old_logins
        
        return self


class UserSearchPydantic(UserPydantic):
    password: SkipJsonSchema[str] = None
    
    async def convert_to_search_model(self, user: User):
        if user is not None:
            self.login = user.login
            self.id = user.id
            self.status = user.status
            self.old_logins = user.old_logins
        return self


class UserSearchPydanticDb(BaseModel):
    user_login: str
