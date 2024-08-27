import asyncio

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from src.core.config import settings
from src.db_models import Base


class DataBaseHelper:
    def __init__(self, db_url, db_echo: bool = False):
        self.engine = create_async_engine(
            url = db_url,
            echo = db_echo
        )
        self.session_factory = async_sessionmaker(
            bind = self.engine,
            autoflush = False,
            autocommit = False,
            expire_on_commit = False
        )


db_helper = DataBaseHelper(db_url = settings.db_url, db_echo = False)


async def start() -> None:
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

# asyncio.run(start())
