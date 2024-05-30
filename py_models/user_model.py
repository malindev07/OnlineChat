from dataclasses import dataclass, field
from itertools import count


@dataclass(frozen = True, slots = True)
class UserLogin:
    value: str


@dataclass(frozen = True, slots = True)
class UserID:
    value: int = 0


@dataclass(frozen = False, slots = True)
class User:
    login: UserLogin
    password: str
    id: UserID = field(default_factory = count(1).__next__)
    
    def hello_user(self):
        print(f'Hello, {self.login}')
    
    # методы прописать
