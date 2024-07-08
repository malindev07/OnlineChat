from dataclasses import dataclass, field
from storage.chats_storage import ChatsStorage
from storage.message_storage import MessageStorage
from storage.users_storage import UsersStorage


@dataclass
class Storage:
    chats_storage: ChatsStorage = field(default_factory = list)
    users_storage: UsersStorage = field(default_factory = list)
    message_storage: MessageStorage = field(default_factory = list)
