from dataclasses import dataclass, field
from itertools import count


@dataclass(frozen = True, slots = True)
class ChatID:
    value: int


@dataclass
class Chat:
    id: ChatID = field(default_factory = count(1).__next__)
    users: list = field(default_factory = list)
    messages: list = field(default_factory = list)
