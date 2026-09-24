import dotenv
import os

from langchain.agents import create_agent
from sqlalchemy import create_engine
from sqlalchemy import create_engine

from src.domain.models.base import Base

dotenv.load_dotenv()
from src.agent.agent import Agent
from langgraph.checkpoint.postgres import PostgresSaver
from contextlib import asynccontextmanager
from fastapi import FastAPI

DATABASE_URL = os.environ.get("DATABASE_URL")

engine = create_engine(DATABASE_URL)

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
        host="127.0.0.1",
        port=8000,
        reload=True,
    )


if __name__ == '__main__':
    main()


