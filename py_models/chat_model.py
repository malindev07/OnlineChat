from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Mapping, MutableMapping, Sequence, MutableSequence
from _collections_abc import Sequence
from py_models.user_model import User, UserLogin


@dataclass(frozen = True, slots = True)
class ChatID:
    value: int


@dataclass(frozen = True, slots = True)
class Message:
    user: UserLogin
    msg_text: str
    created_at: datetime = field(default_factory = datetime.now)


@dataclass(frozen = True, slots = True)
class Chat:a
    id: ChatID
    users: List[UserLogin] = field(default_factory = list)
    messages: MutableSequence[Message] = field(default_factory = list)
    
    # сделать методы
