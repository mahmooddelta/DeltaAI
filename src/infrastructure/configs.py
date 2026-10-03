import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    APP_HOST: str = os.getenv("APP_HOST", "127.0.0.1")
    APP_PORT: int = int(os.getenv("APP_PORT", "8070"))
    APP_RELOAD: bool = os.getenv("APP_RELOAD", "true").lower() in ("1", "true", "yes")

    DATABASE_URL: str | None = os.getenv("DATABASE_URL")
    LANGGRAPH_DATABASE_URL: str | None = os.getenv("LANGGRAPH_DATABASE_URL")


config = Config()
