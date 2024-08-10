from typing import TYPE_CHECKING, List

from sqlalchemy import ForeignKey, Column, ARRAY, String
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column

from db_models.base import Base

if TYPE_CHECKING:
    from .message_model_db import Message
    from .user_model_db import User


class Chat(Base):
    __tablename__ = 'chats'
    chat_id: Mapped[int] = mapped_column(primary_key = True)
    users = Column(ARRAY(String))
    messages = Column(ARRAY(String))

# class ChatUsers(sqlalchemy.schema.Table):
#     chat_id: Mapped[int] = mapped_column(ForeignKey('chats.chat_id'))
#     user_1_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'))
#     user_2_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'))
