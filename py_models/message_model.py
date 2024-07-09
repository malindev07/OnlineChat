from dataclasses import dataclass, field
from itertools import count
import datetime


@dataclass
class MessageID:
    value: int


@dataclass
class MessageUserLogin:
    login: str


@dataclass
class MessageText:
    text: str


@dataclass
class MessageChatId:
    id: int


@dataclass
class Message:
    user_login: MessageUserLogin
    chat_id: MessageChatId
    text: MessageText
    date: datetime
    
    # id: MessageID = field(default_factory = count(1).__next__)


@dataclass
class MessageForStorage:
    text: MessageText
    date: datetime


@dataclass
class MessageForChatStorage:
    user_login: MessageUserLogin
    text: MessageText
    date: datetime
