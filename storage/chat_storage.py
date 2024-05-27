from dataclasses import dataclass, field

from py_models.chat_model import Chat, ChatID
from py_models.user_model import User, UserID, UserLogin


@dataclass
class StorageChat:
    _chats: dict[ChatID, Chat] = field(default_factory = dict)
    
    # прописать методы
