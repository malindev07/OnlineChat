import dataclasses
from dataclasses import dataclass


@dataclass(frozen = True, slots = True)
class UserID:
    value: int


@dataclass(frozen = True, slots = True)
class UserLogin:
    value: str


@dataclass(frozen = True, slots = True)
class User:
    id: UserID
    login: UserLogin
    password: str
    
    def hello_user(self):
        print(f'Hello, {self.login}')
    
    # методы прописать


user_id = User(UserID(2), UserLogin('str'), 'pass')

print(user_id.id)
