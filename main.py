from sqlalchemy import create_engine

from src.domain.models.base import Base
from src.infrastructure.configs import config
from contextlib import asynccontextmanager
from fastapi import FastAPI

engine = create_engine(config.DATABASE_URL)

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)

    yield

app = FastAPI(
    title="Delta AI",
    description="AI Agent API",
    version="1.0.0",
)


@app.get("/health")
def health():
    return {"status": "ok"}


def main():

    # with PostgresSaver.from_conn_string(DATABASE_URL) as checkpointer:
    #     checkpointer.setup()
    #     agent = Agent(checkpointer)
    #     agent.chat_loop()
    import uvicorn

    uvicorn.run(
        "main:app",
        host=config.APP_HOST,
        port=config.APP_PORT,
        reload=config.APP_RELOAD,
    )


if __name__ == '__main__':
    main()


