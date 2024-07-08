from py_models.message_model import Message, MessageUserLogin, MessageChatId, MessageText
from pydantic_models.pydantic_message_model import MessageEntryPydantic, MessageExitPydantic


def convert_pyd_to_dataclass(message: MessageEntryPydantic) -> Message:
    entry_msg_model = Message(
        user_login = MessageUserLogin(value = message.user_login),
        chat_id = MessageChatId(value = message.chat_id),
        text = MessageText(value = message.msg_text)
    )
    
    return entry_msg_model


def convert_dataclass_to_pyd(message: Message) -> MessageExitPydantic:
    exit_msg_model = MessageExitPydantic(
        user_login = message.user_login.value, msg_text = message.text.value
    )
    return exit_msg_model
