from pydantic_settings import BaseSettings


class Setting(BaseSettings):
    db_url: str = "postgresql+asyncpg://postgres:postgres@localhost/OnlineChat"
    
    db_echo: bool = False


settings = Setting()
