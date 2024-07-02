from dataclasses import dataclass, field
from py_models.chat_model import ChatID, Chat
from pydantic_models.pydantic_user_model import UserSearchPydantic
from py_models.user_model import User
from storage.users_storage import UsersStorage


def check_users_in_storage(users: [UserSearchPydantic], users_storage: UsersStorage) -> (bool, list[User]):
    i = 0
    checked_users: list[User] = []
    for user in users:
        for val in users_storage.users:
            for k in val:
                if user.login == k:
                    checked_users.append(val)
                    i += 1
    if i == len(users):
        return True, checked_users


@dataclass
class ChatsStorage:
    chats: [dict[ChatID, Chat]] = field(default_factory = list)
    
    def create_chat(self, users: [UserSearchPydantic], users_storage: UsersStorage) -> Chat:
        print(check_users_in_storage(users, users_storage))
        if check_users_in_storage(users, users_storage)[0]:
            new_chat = Chat()
            for user in check_users_in_storage(users, users_storage)[1]:
                new_chat.users.append(user)
            self.chats.append({new_chat.id: new_chat})
            return new_chat
