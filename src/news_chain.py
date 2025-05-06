from langchain_ollama import ChatOllama
from langchain_community.tools import DuckDuckGoSearchRun

def get_news_analysis(query: str):
    llm = ChatOllama(
        model = "llama3.2:latest",
        temperature = 0.8,
    )

    search = DuckDuckGoSearchRun()
    result = search.invoke("What are the latest news on {query}")

    llm_response = llm.invoke(f"""
You are a financial expert and news analyst. Here's a query: What are the latest news on {query}
The following are the latest articles related to the query:
{result}

Based on these articles, provide a detailed analysis of the current news trends, potential impacts, and any key takeaways.
""")
    
    return llm_response.content