
from langchain_tavily import TavilySearch
import dotenv


dotenv.load_dotenv()


tavily_search = TavilySearch(
    max_results=1
)