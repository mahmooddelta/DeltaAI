import dotenv
import os

dotenv.load_dotenv()
from src.agent.agent import Agent
from langgraph.checkpoint.postgres import PostgresSaver

DATABASE_URL = os.environ.get("LANGGRAPH_DATABASE_URL")



def main():

    with PostgresSaver.from_conn_string(DATABASE_URL) as checkpointer:
        checkpointer.setup()
        agent = Agent(checkpointer)
        agent.chat_loop()


if __name__ == '__main__':
    main()


