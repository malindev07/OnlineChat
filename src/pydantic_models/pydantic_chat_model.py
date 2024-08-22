from typing import Optional
from src.db_models import Chat as Chat_DB

from pydantic import BaseModel


class ChatPydantic(BaseModel):
    id: int
    users: list
    messages: Optional[list]
    
    def convert_to_pydantic_model(self, chat: Chat_DB):
        self.id = chat.chat_id
        self.users = chat.users
        self.messages = chat.messages
