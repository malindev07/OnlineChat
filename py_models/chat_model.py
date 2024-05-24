import datetime
from typing import List

from py_models.user_model import User


class Message:
    user: User
    created_at: datetime.datetime
    msg_text: str


class Chat:
    id: int
    users: List[User]
    messages: List[Message]
    messages_text: List[str]
