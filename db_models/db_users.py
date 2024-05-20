from sqlalchemy.orm import Mapped, mapped_column

from db_models import Base


class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key = True)
    login: Mapped[str]
    password: Mapped[str]
