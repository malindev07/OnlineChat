from pydantic import BaseModel
from pydantic.json_schema import SkipJsonSchema


class MessageEntryPydantic(BaseModel):
    msg_text: str
    user_login: str
    chat_id: SkipJsonSchema[int] = None


class MessageExitPydantic(BaseModel):
    user_login: str
    msg_text: str
