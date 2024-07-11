from dataclasses import dataclass, field
from py_models.chat_model import ChatID, Chat

from pydantic_models.pydantic_user_model import UserSearchPydantic
from py_models.user_model import User
from storage.users_storage import UsersStorage


async def check_users_in_storage(users: [UserSearchPydantic], users_storage: UsersStorage) -> (bool, list[User]):
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


async def check_chat_in_user(users: list[User]) -> int | bool | None:
    check_list = []
    tuples = set()
    for user in users:
        
        for k in user:
            tuples.add(k)
            
            if user[k].chats_id is not None:
                for i in user[k].chats_id:
                    check_list.append(i)
            else:
                user[k].chats_id = []
    print(len(tuples))
    print(len(tuples) == 1)
    if len(tuples) == 1:
        return None
    else:
        count = 0
        for i in check_list:
            for k in check_list:
                if i == k:
                    count += 1
            if count == len(users):
                return i
            else:
                count = 0
        if count == 0:
            return False
    # return False


@dataclass
class ChatsStorage:
    chats: list[dict[ChatID, Chat]] = field(default_factory = list)
    
    async def create_chat(self, users: [UserSearchPydantic], users_storage: UsersStorage) -> Chat | None:
        
        res = await check_users_in_storage(users, users_storage)
        check_res = await check_chat_in_user(res[1])
        if res[0]:
            if check_res:
                for i in self.chats:
                    for k in i:
                        if k == check_res:
                            for chat in self.chats:
                                for chat_id in chat:
                                    if chat_id == k:
                                        print('Уже в чате')
                                        return chat[chat_id]
            elif check_res is None:
                print('Нельзя создать чат')
                return None
            
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
