from langchain_ollama import ChatOllama
from src.stock_data import get_stock_data_by_period
from src.news_chain import get_news_analysis as get_news_analysis_chain
from src.analyze_sentiment import get_sentiment_analysis

def get_financial_advisor(stock_symbol: str) -> str:
    """ 
    Provides financial advice based on stock symbol by fetching stock data and analyzing sentiment.
    
    Arguments:
        stock_symbol (str): The stock symbol to provide financial advice for.

    Returns:
        str: Simulated financial advice based on data and sentiment analysis.
    """
    llm = ChatOllama(
        model="llama3.2:latest",
        temperature=0.2,
    )
    stock_data = get_stock_data_by_period(stock_symbol, time_period="1mo")
    
    news_analysis = get_news_analysis_chain(stock_symbol)
    
    sentiment = get_sentiment_analysis(news_analysis)

    prompt = f"""
    You are a financial advisor. Based on the following data and news for the stock symbol {stock_symbol}, provide concise financial advice.
    
    Stock Data (last month): {stock_data}

    Recent News: {news_analysis}

    Recent News Sentiment: {sentiment}
    
    Your advice should consider the stock's recent performance, sentiment, and any upcoming market trends.
    """
    
    response = llm.invoke(prompt)
    return response.content
