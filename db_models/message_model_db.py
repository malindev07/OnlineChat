import datetime
from typing import TYPE_CHECKING, Optional
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey
from db_models.base import Base

if TYPE_CHECKING:
    from db_models import Chat, User


class Message(Base):
    __tablename__ = 'messages'
    id: Mapped[int] = mapped_column(primary_key = True)
    chat_id: Mapped[int] = mapped_column(ForeignKey('chats.chat_id', ondelete = 'CASCADE'))
    chat: Mapped["Chat"] = relationship(back_populates = "messages")
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id", ondelete = 'CASCADE'))
    user_login: Mapped[Optional[str]]
    text: Mapped[str]
    date: Mapped[datetime.datetime]
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
