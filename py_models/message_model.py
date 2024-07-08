from dataclasses import dataclass, field
from itertools import count


@dataclass
class MessageID:
    value: int


@dataclass
class MessageUserLogin:
    value: str


@dataclass
class MessageText:
    value: str


@dataclass
class MessageChatId:
    value: int


@dataclass
class Message:
    user_login: MessageUserLogin
    chat_id: MessageChatId
    text: MessageText
    
    # id: MessageID = field(default_factory = count(1).__next__)
