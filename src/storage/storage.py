from dataclasses import dataclass

from src.storage.chats_storage import ChatsStorage
from src.storage.message_storage import MessageStorage
from src.storage.users_storage import UsersStorage


@dataclass
class Storage:
    chats_storage: ChatsStorage
    users_storage: UsersStorage
    message_storage: MessageStorage
