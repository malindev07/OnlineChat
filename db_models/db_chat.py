import datetime

from sqlalchemy import ForeignKey, text, create_engine, DateTime, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db_models.db_base import Base
from db_models.db_users import User


class Message(Base):
    __tablename__ = "message"
    
    user: Mapped[str]
    message: Mapped[str]
    created_at: Mapped[datetime.datetime] = mapped_column(server_default = text("TIMEZONE('utc', now())"))
    messages_id: Mapped[int] = mapped_column(ForeignKey("messages.id"), nullable = True)


#
class Messages(Base):
    __tablename__ = "messages"
    
    messages: Mapped[list["Message"]] = relationship(back_populates = 'message', cascade = "all, delete", )
    chat_id: Mapped[int] = mapped_column(ForeignKey("chats.id"))


class Chat(Base):
    __tablename__ = "chats"
    
    users: Mapped[list["User"]] = mapped_column(ForeignKey("user.id"))
    messages_id: Mapped[int] = mapped_column(ForeignKey("messages.id"))


engine = create_engine("postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/OnlineChat", echo = True)

Base.metadata.create_all(engine)
