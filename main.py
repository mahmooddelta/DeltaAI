import dotenv

from src.services.chat_bot_service import ChatBotService
from src.agent.agent import Agent
from langgraph.checkpoint.postgres import PostgresSaver
import os

dotenv.load_dotenv()


def main():

    db_url = os.environ.get("DATABASE_URL")

    with PostgresSaver.from_conn_string(db_url) as checkpointer:
        checkpointer.setup()
        agent = Agent(checkpointer)
        agent.chat_loop()


if __name__ == '__main__':
    main()


