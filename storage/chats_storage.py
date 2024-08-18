from dataclasses import dataclass, field

from db_actions.actions_message_db import show_chat_msgs
from db_actions.actions_user_db import search_user_db
from db_actions.actions_chat_db import create_chat_db, check_last_index_chat_db, return_chat_by_id_db
from py_models.chat_model import ChatID, Chat

from pydantic_models.pydantic_user_model import UserSearchPydanticDb
from py_models.user_model import User


# async def check_users_in_storage(users: [UserSearchPydantic], users_storage: UsersStorage = None) -> (bool, list[User]):
#     for user in users:
#         res = await search_user_db(user)
#         print(res)
# i = 0
# checked_users: list[User] = []
# for user in users:
#     for val in users_storage.users:
#         for k in val:
#             if user.login == k:
#                 checked_users.append(val)
#                 i += 1
# if i == len(users):
#     return [True, checked_users]
# else:
#     return [False, checked_users]


# async def check_chat_in_user(users: list[User]) -> int | bool | None:
#     check_list = []
#     tuples = set()
#     for user in users:
#
#         for k in user:
#             tuples.add(k)
#
#             if user[k].chats_id is not None:
#                 for i in user[k].chats_id:
#                     check_list.append(i)
#             else:
#                 user[k].chats_id = []
#
#     if len(tuples) == 1:
#         return None
#     else:
#         count = 0
#         for i in check_list:
#             for k in check_list:
#                 if i == k:
#                     count += 1
#             if count == len(users):
#                 return i
#             else:
#                 count = 0
#         if count == 0:
#             return False


@dataclass
class ChatsStorage:
    chats: list[dict[ChatID, Chat]] = field(default_factory = list)
    
    @staticmethod
    async def check_users_in_storage(users: [UserSearchPydanticDb]):
        bool_res = set()
        for user in users:
            res = await search_user_db(user.user_login)
            bool_res.add(res)
        if len(bool_res) > 1:
            return None
        else:
            return True
    
    @staticmethod
    async def create_chat(users: [UserSearchPydanticDb]):
        for user in users:
            res = await search_user_db(user.user_login)
            
            if res is None:
                print('Один из пользоватлей не найден')
                return None
        
        users_logins = []
        for user in users:
            users_logins.append(user.user_login)
        
        new_chat = Chat()
        new_chat.id = await check_last_index_chat_db()
        
        for user in users_logins:
            new_chat.users.append(user)
        
        res = await create_chat_db(new_chat)
        print(res)
        return res
    
    @staticmethod
    async def show_chat_msg_storage(chat_id: int):
        res = await show_chat_msgs(chat_id)
        return res
    
    @staticmethod
    async def return_chat_by_id(chat_id: int):
        res = await return_chat_by_id_db(chat_id)
        return res
    # async def create_chat(self, users: [UserSearchPydantic], users_storage: UsersStorage) -> Chat | None | int:
    #
    #     res = await check_users_in_storage(users, users_storage)
    #     check_res = await check_chat_in_user(res[1])
    #     if res[0]:
    #         if check_res:
    #             for i in self.chats:
    #                 for k in i:
    #                     if k == check_res:
    #                         for chat in self.chats:
    #                             for chat_id in chat:
    #                                 if chat_id == k:
    #                                     print('Уже в чате')
    #                                     return chat_id
    #         elif check_res is None:
    #             print('Нельзя создать чат')
    #             return None
    #
    #         else:
    #             new_chat = Chat()
    #             for user in res[1]:
    #                 for k in user:
    #                     user[k].chats_id.append(new_chat.id)
    #
    #                 new_chat.users.append(user)
    #             self.chats.append({new_chat.id: new_chat})
    #
    #             return new_chat
    #     else:
    #         return None
    
    # def show_chat_msg(self, search_chat_id: int) -> list:
    #     for chat in self.chats:
    #         if search_chat_id in chat:
    #             return chat[search_chat_id].messages
