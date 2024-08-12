from dataclasses import dataclass, field
from itertools import count
from typing import Optional

from py_models.message_model import MessageForChatStorage


@dataclass(frozen = True, slots = True)
class ChatID:
    value: int


@dataclass
class Chat:
    id: Optional[ChatID] = field(default_factory = int)
    users: list = field(default_factory = list)
    messages: list[MessageForChatStorage] = field(default_factory = list)
