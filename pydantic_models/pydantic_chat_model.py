from itertools import count

from pydantic import BaseModel, Field

from py_models.chat_model import ChatID


class ChatPydantic(BaseModel):
    id: ChatID
    users: list
    messages: list
