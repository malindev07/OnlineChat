from dataclasses import dataclass, field

from py_models.chat_model import Chat, ChatID
from py_models.user_model import User, UserID, UserLogin


@dataclass
class StorageUser:
    _users: dict[UserLogin, User] = field(default_factory = dict)
    
    def add_user(self, login: UserLogin, password: str):
        pass
