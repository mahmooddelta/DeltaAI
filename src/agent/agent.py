from langchain_openai import ChatOpenAI
from langgraph.checkpoint.postgres import PostgresSaver
from langchain.agents import create_agent
from tools.weather import get_weather
from tools.tavily_search import tavily_search


class Agent:
    def __init__(self, checkpointer):
        self.llm = ChatOpenAI(
            model="gpt-5.6",
            temperature=0.5
        )

        self.agent = create_agent(
            model=self.llm,
            tools=[get_weather, tavily_search],
            system_prompt="",
            checkpointer=checkpointer
        )
