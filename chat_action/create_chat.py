from typing import List

from py_models.chat_model import Chat, Message
from py_models.user_model import User


def create_chat(users: List[User]) -> Chat:
    new_chat = Chat()
    new_chat.users = users
    return new_chat
