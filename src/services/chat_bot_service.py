from langchain_openai import ChatOpenAI

class ChatBotService:
    def __init__(self):
        self.chat_openai = ChatOpenAI(
            model="gpt-5.6",
            temperature=0.5
        )

    def chat(self):
        return self.chat_openai.invoke("hi my name is mahmood")


