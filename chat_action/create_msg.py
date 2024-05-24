import datetime

from py_models.chat_model import Message, Chat


def create_new_msg(user: str, user_id: int, msg_text: str) -> Message:
    new_msg = Message()
    new_msg.user = user
    new_msg.user_id = user_id
    new_msg.created_at = datetime.datetime.now(datetime.UTC)
    new_msg.msg = msg_text
    
    return new_msg
