from dataclasses import dataclass, field
from typing import Optional

from src.py_models.chat_model import ChatID


@dataclass
class UserLogin:
    value: str


@dataclass
class UserID:
    value: int


@dataclass
class User:
    login: UserLogin
    password: str
    chats_id: Optional[list[ChatID]] = list
    id: UserID = field(default = 0)
    status: Optional[str] = None
    
    old_logins: Optional[list[UserLogin]] = None
