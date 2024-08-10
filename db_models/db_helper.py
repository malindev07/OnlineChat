from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from core.config import settings


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


db_helper = DataBaseHelper(db_url = settings.db_url, db_echo = True)
