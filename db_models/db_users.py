from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

from db_models.db_base import Base


# from db_models.db_chat import Base


class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key = True)
    login: Mapped[str]
    password: Mapped[str]
