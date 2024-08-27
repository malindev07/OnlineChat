from typing import TYPE_CHECKING, Optional

from sqlalchemy import Column, ARRAY, String
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column

from src.db_models.base import Base

if TYPE_CHECKING:
    from .message_model_db import Message


class Chat(Base):
    __tablename__ = 'chats'
    chat_id: Mapped[int] = mapped_column(primary_key = True)
    users = Column(ARRAY(String))
    messages: Mapped[list["Message"]] = relationship(back_populates = "chat")
    
    ## test migrations
    # test1: Mapped[Optional[str]]
