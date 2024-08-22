from pydantic import BaseModel
from pydantic.json_schema import SkipJsonSchema


class MessageEntryPydantic(BaseModel):
    chat_id: int
    user_id: int
    text: str


class MessageExitPydantic(BaseModel):
    user_login: str
    msg_text: str
