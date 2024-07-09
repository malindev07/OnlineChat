from pydantic import BaseModel
from pydantic.json_schema import SkipJsonSchema


class MessageEntryPydantic(BaseModel):
    msg_text: str
    user_login: str
    chat_id: int


class MessageExitPydantic(BaseModel):
    user_login: str
    msg_text: str
