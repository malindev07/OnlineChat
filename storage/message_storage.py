from dataclasses import dataclass, field

from py_models.message_model import MessageUserLogin, MessageText, Message, MessageChatId


@dataclass
class MessageStorage:
    msg_storage: list[dict[MessageUserLogin, Message]] = field(default_factory = list)
    
    def create_message(self, msg: Message) -> Message:
        new_msg = Message(user_login = msg.user_login, chat_id = msg.chat_id, text = msg.text)
        self.msg_storage.append({new_msg.user_login.value: new_msg})
        return new_msg
    
    def show_msg_storage(self) -> list[dict[MessageUserLogin, Message]]:
        return self.msg_storage
