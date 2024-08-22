from dataclasses import dataclass, field

from src.db_actions.actions_message_db import create_message_db, show_chat_msgs
from src.py_models.message_model import MessageUserLogin, MessageChatId, MessageForStorage
from src.pydantic_models import MessageExitPydantic


# async def add_message_to_chat(chat_storage: ChatsStorage, message: Message):
#     for item in chat_storage.chats:
#         for k in item:
#             if k == message.chat_id.id:
#                 add_msg = MessageForChatStorage(text = message.text.text, user_login = message.user_login.login,
#                                                 date = message.date)
#                 item[k].messages.append(add_msg)


@dataclass
class MessageStorage:
    msg_storage: dict[MessageChatId, dict[MessageUserLogin, list[MessageForStorage]]] = field(default_factory = dict)
    
    # msg_storage: list[dict[MessageUserLogin, Message]] = field(default_factory = list)
    # async def create_message(self, msg: Message) -> Message:
    #     new_msg = MessageForStorage(text = msg.text.text, date = msg.date)
    #
    #     if msg.chat_id.id in self.msg_storage.keys():
    #         if msg.user_login.login in self.msg_storage[msg.chat_id.id]:
    #             self.msg_storage[msg.chat_id.id][msg.user_login.login].append(new_msg)
    #
    #         else:
    #             self.msg_storage[msg.chat_id.id][msg.user_login.login] = [new_msg]
    #     else:
    #         self.msg_storage[msg.chat_id.id] = {msg.user_login.login: [new_msg]}
    #
    #     return msg
    @staticmethod
    async def create_message(user_id: int, chat_id: int, text: str) -> MessageExitPydantic:
        res = await create_message_db(chat_id = chat_id, user_id = user_id, text = text)
        
        msg_res = MessageExitPydantic(user_login = res['user_login'], msg_text = res['text'])
        
        return msg_res
    
    @staticmethod
    async def show_chats_messages(chat_id: int) -> list[dict]:
        res = await show_chat_msgs(chat_id = chat_id)
        return res
