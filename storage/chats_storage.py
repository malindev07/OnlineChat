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
        return [True, checked_users]
    else:
        return [False, checked_users]


def check_chat_in_user(users: list[User]) -> bool | int:
    check_list = []
    for user in users:
        for k in user:
            if user[k].chats_id is not None:
                for i in user[k].chats_id:
                    check_list.append(i)
            else:
                user[k].chats_id = []
    
    count = 0
    for i in check_list:
        for k in check_list:
            if i == k:
                count += 1
        if count == len(users):
            return i
        else:
            count = 0
    return False


@dataclass
class ChatsStorage:
    chats: list[dict[ChatID, Chat]] = field(default_factory = list)
    
    def create_chat(self, users: [UserSearchPydantic], users_storage: UsersStorage) -> Chat | None:
        
        res = check_users_in_storage(users, users_storage)
        # print(res)
        
        if res[0]:
            if check_chat_in_user(res[1]):
                for i in self.chats:
                    for k in i:
                        if k == check_chat_in_user(res[1]):
                            for chat in self.chats:
                                for chat_id in chat:
                                    if chat_id == k:
                                        return chat
                
                print('Уже в чате')
            else:
                new_chat = Chat()
                for user in res[1]:
                    for k in user:
                        user[k].chats_id.append(new_chat.id)
                    
                    new_chat.users.append(user)
                self.chats.append({new_chat.id: new_chat})
                return new_chat
        else:
            return None
