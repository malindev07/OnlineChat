from dataclasses import dataclass, field
from itertools import count
from typing import Optional

from py_models.chat_model import ChatID


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
    id: UserID = field(default = 0)
    status: Optional[str] = None
    chats_id: Optional[list[ChatID]] = None
    old_logins: Optional[list[UserLogin]] = None
