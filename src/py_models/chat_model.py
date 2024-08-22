from dataclasses import dataclass, field
from typing import Optional

from src.py_models.message_model import MessageForChatStorage


@dataclass(frozen = True, slots = True)
class ChatID:
    value: int


@dataclass
class Chat:
    id: Optional[ChatID] = field(default_factory = int)
    users: list[str] = field(default_factory = list[str])
    messages: list[MessageForChatStorage] = field(default_factory = list)
