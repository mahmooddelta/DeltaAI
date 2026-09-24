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
            user_input = input("Ask anything: (type 'q' to quit or 'ch' for change session): ")


            if user_input == "q":
                print("Goodbye")
                break

            # if user_input == "ch":
            #     active_session = "session_2" if active_session == "session_1" else "session_1"
            #     continue

            # self.messages.append(HumanMessage(user_input))
            config = {'configurable': {'thread_id': session}}
            response = self.agent.invoke({
                "messages": HumanMessage(user_input)
            }, config=config)

            # self.messages.append(response['messages'][-1])
            print(response['messages'][-1].content)

        messages_config = {'configurable': {'thread_id': active_session}}
        state = self.agent.get_state(messages_config)
        print(state.values['messages'])

