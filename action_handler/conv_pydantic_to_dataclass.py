import datetime

from py_models.chat_model import Chat
from py_models.message_model import Message, MessageUserLogin, MessageChatId, MessageText
from pydantic_models.pydantic_chat_model import ChatPydantic
from pydantic_models.pydantic_message_model import MessageEntryPydantic, MessageExitPydantic


async def convert_pyd_to_dataclass(message: MessageEntryPydantic) -> Message:
    entry_msg_model = Message(
        user_login = MessageUserLogin(login = message.user_login),
        chat_id = MessageChatId(id = message.chat_id),
        text = MessageText(text = message.msg_text),
        date = datetime.datetime.now()
    
    )
    
    return entry_msg_model


async def convert_dataclass_to_pyd(message: Message) -> MessageExitPydantic:
    exit_msg_model = MessageExitPydantic(
        user_login = message.user_login.login, msg_text = message.text.text
    )
    return exit_msg_model


def convert_dataclass_chat_to_pyd(chat: Chat) -> ChatPydantic | None:
    if chat is not None:
        print(ChatPydantic(id = chat.id, users = chat.users, messages = chat.messages))
        chat_pyd = ChatPydantic(id = chat.id, users = chat.users, messages = chat.messages)
    else:
        return None
    return chat_pyd
