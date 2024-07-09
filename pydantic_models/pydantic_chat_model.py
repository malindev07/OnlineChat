from itertools import count

from pydantic import BaseModel, Field


class ChatPydantic(BaseModel):
    id: int
    users: list
    messages: list
