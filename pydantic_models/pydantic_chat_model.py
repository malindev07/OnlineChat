from itertools import count

from pydantic import BaseModel, Field

from py_models.chat_model import ChatID


class ChatPydantic(BaseModel):
    id: ChatID = Field(default_factory = count(1).__next__)
    users: list
    messages: list
