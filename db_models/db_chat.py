import datetime
from typing import List

from sqlalchemy import ForeignKey, func, text, JSON
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

from db_models import Base
from db_models.db_users import User


class Message(Base):
    __tablename__ = "message"
    
    user: Mapped[User]
    message: Mapped[str]
    created_at: Mapped[datetime.datetime] = mapped_column(server_default = text("TIMEZONE('utc', now())"))
    messages_id: Mapped[int] = mapped_column(ForeignKey("messages.id"))


#
class Messages(Base):
    __tablename__ = "messages"
    
    id: Mapped[int] = mapped_column(primary_key = True)
    messages: Mapped[List["Message"]]
    chat_id: Mapped[int] = mapped_column(ForeignKey("chats.id"))


class Chat(Base):
    __tablename__ = "chats"
    
    id: Mapped[int] = mapped_column(primary_key = True)
    users: Mapped[List["User"]]
    messages_id: Mapped[int] = mapped_column(ForeignKey("messages.id"))
