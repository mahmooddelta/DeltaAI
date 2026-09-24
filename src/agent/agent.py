from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.postgres import PostgresSaver
from langchain.agents import create_agent
from src.agent.tools.weather import get_weather
from src.agent.tools.tavily_search import tavily_search
from src.prompt.prompts import SYSTEM_PROMPT
import uuid


class Agent:
    def __init__(self, checkpointer):
        self.llm = ChatOpenAI(
            model="gpt-5.6",
            temperature=0.5,
            use_responses_api=True,
        )

        self.agent = create_agent(
            model=self.llm,
            tools=[get_weather, tavily_search],
            system_prompt=SYSTEM_PROMPT,
            checkpointer=checkpointer
        )

    def chat_loop(self):

        session_key = input("Enter Session : ")
        session = str(uuid.uuid4()) if session_key=="" else session_key
        while True:
            user_input = input("Ask anything: (type 'q' to quit): ")

            if user_input == "q":
                print("Goodbye")
                break

            config = {'configurable': {'thread_id': session}}
            response = self.agent.invoke({
                "messages": HumanMessage(user_input)
            }, config=config)

            print(response['messages'][-1].content)

        messages_config = {'configurable': {'thread_id': session}}
        state = self.agent.get_state(messages_config)
        print(state.values['messages'])

