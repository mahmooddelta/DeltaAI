from src.agent.agent import Agent
from src.infrastructure.configs import config
from langgraph.checkpoint.postgres import PostgresSaver


def main():

    with PostgresSaver.from_conn_string(config.LANGGRAPH_DATABASE_URL) as checkpointer:
        checkpointer.setup()
        agent = Agent(checkpointer)
        agent.chat_loop()


if __name__ == '__main__':
    main()


