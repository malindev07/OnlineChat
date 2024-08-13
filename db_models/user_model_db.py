from typing import Optional, TYPE_CHECKING

from sqlalchemy import ARRAY, String, Integer, Column
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column

from db_models.base import Base

if TYPE_CHECKING:
    from db_models import Message


class User(Base):
    __tablename__ = 'users'
    user_id: Mapped[int] = mapped_column(primary_key = True)
    login: Mapped[str]
    password: Mapped[str]
    status: Mapped[Optional[str]]
    chats_id = Column(ARRAY(Integer))
    old_logins = Column(ARRAY(String))
