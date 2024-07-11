from dataclasses import dataclass, field

from py_models.message_model import MessageUserLogin, Message, MessageChatId, MessageForStorage, \
    MessageForChatStorage
from storage.chats_storage import ChatsStorage


async def add_message_to_chat(chat_storage: ChatsStorage, message: Message):
    for item in chat_storage.chats:
        for k in item:
            if k == message.chat_id.id:
                add_msg = MessageForChatStorage(text = message.text.text, user_login = message.user_login.login,
                                                date = message.date)
                item[k].messages.append(add_msg)
                print(item[k].messages)


@dataclass
class MessageStorage:
    msg_storage: dict[MessageChatId, dict[MessageUserLogin, list[MessageForStorage]]] = field(default_factory = dict)
    
    # msg_storage: list[dict[MessageUserLogin, Message]] = field(default_factory = list)
    async def create_message(self, msg: Message) -> Message:
        new_msg = MessageForStorage(text = msg.text.text, date = msg.date)
        
        if msg.chat_id.id in self.msg_storage.keys():
            if msg.user_login.login in self.msg_storage[msg.chat_id.id]:
                self.msg_storage[msg.chat_id.id][msg.user_login.login].append(new_msg)
            
            else:
                self.msg_storage[msg.chat_id.id][msg.user_login.login] = [new_msg]
        else:
            self.msg_storage[msg.chat_id.id] = {msg.user_login.login: [new_msg]}
        
        return msg
    
    async def show_msg_storage(self) -> dict[MessageChatId, dict[MessageUserLogin, list[MessageForStorage]]]:
        return self.msg_storage
