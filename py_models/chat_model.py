import datetime
from typing import List

from db_models.db_users import User


class Message:
    user: str
    user_id: int
    created_at: datetime.datetime
    msg: str


class Chat:
    id: int
    users: List[User]
    messages: List[Message]
