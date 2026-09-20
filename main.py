import dotenv

from src.services.chat_bot_service import ChatBotService

dotenv.load_dotenv()


def main():
    chat_service = ChatBotService()
    chat = chat_service.chat()
    print(chat.content)




if __name__ == '__main__':
    main()


