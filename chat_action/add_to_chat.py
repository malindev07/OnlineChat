from py_models.chat_model import Message, Chat


def add_msg_to_chat(msg: Message) -> Chat:
    new_chat = Chat()
    new_chat.users.append(msg.user)
    new_chat.messages.append(msg)
    new_chat.messages_text.append(msg.msg_text)
    
    return new_chat
