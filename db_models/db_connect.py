import asyncio

from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, async_sessionmaker

from db_models.db_base import Base


async def db_connect(driver: str, login: str, password: str) -> AsyncEngine:
    async_engine: AsyncEngine = create_async_engine(
        f"postgresql+{driver}://{login}:{password}@localhost:5432/OnlineChat",
        echo = True,
    )
    
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    return async_engine


async def db_async_sessionmaker(engine: AsyncEngine) -> async_sessionmaker:
    async_session = async_sessionmaker(engine, expire_on_commit = False)
    return async_session
