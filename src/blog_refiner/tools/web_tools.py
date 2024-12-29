from crewai_tools import tool
from tavily import TavilyClient
from dotenv import load_dotenv
import os

load_dotenv()

@tool
def search_web(query: str) -> str:
    """
    Performs a web search using the Tavily API.
    """
    # Initialize Tavily client
    api_key = os.getenv("TAVILY_API_KEY")
    if not api_key:
        return "Tavily API key is missing. Please set it in the .env file."
    
    tavily = TavilyClient(api_key=api_key)
    
    # Perform search
    try:
        results = tavily.search(query)
        return results if results else "No results found."
    except Exception as e:
        return f"Error while searching: {str(e)}"
