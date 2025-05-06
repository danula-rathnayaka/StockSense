from mcp.server.fastmcp import FastMCP

from src.news_chain import get_news_analysis as get_news_analysis_chain
from src.stock_data import get_stock_data_by_dates, get_stock_data_by_period
from src.analyze_sentiment import get_sentiment_analysis
from src.financial_advisor import get_financial_advisor
from src.market_trend import get_market_trends

# Create an MCP server instance
mcp = FastMCP("StockSense")

@mcp.tool()
def get_news(stock_symbol: str) -> str:
    """
    Simulates fetching news for a stock symbol by returning a placeholder analysis.
    
    This function takes a stock symbol, processes it (e.g., reverses the symbol), 
    and returns a simulated news analysis.

    Parameters:
        stock_symbol (str): The stock symbol to find information about

    Returns:
        str: A simulated news analysis
    """
    return get_news_analysis_chain(stock_symbol)

@mcp.tool()
def get_stock_data(stock_symbol: str, time_period: str = "1y", start_date: str = None, end_date: str = None) -> str:
    """
    Simulate stock data retrieval by calculating the length of the stock symbol 
    and returning additional information based on the time period or date range.
    
    This function mimics the process of fetching stock data for a given stock symbol.
    Instead of actually retrieving real stock data, it simulates the data retrieval 
    by calculating and returning the length of the stock symbol, and provides information
    about the time period or date range passed in.

    Args:
        stock_symbol (str): The stock symbol (e.g., 'AAPL', 'GOOG') to simulate data retrieval.
        time_period (str, optional): The time period to simulate data for. Default is "1y".
                                     Valid options are (1d, 5d, 1mo, 3mo, 6mo, 1y, 5y, 10y, ytd, max)
        start_date (str, optional): The start date for the simulated date range in 'YYYY-MM-DD' format.
        end_date (str, optional): The end date for the simulated date range in 'YYYY-MM-DD' format.

    Returns:
        str: A string representing the simulated stock data, including:
             - The length of the stock symbol
             - The time period or date range information.
    
    Example:
        get_stock_data("AAPL", time_period="1mo")
        # Returns: "Simulating data for AAPL for the time period 1mo. Length of symbol: 4"

        get_stock_data("AAPL", start_date="2025-04-01", end_date="2025-04-10")
        # Returns: "Simulating data for AAPL from 2025-04-01 to 2025-04-10. Length of symbol: 4"
    """
    # Simulate the data retrieval based on the time period or date range
    if start_date and end_date:
        return get_stock_data_by_dates(stock_symbol, start_date, end_date)
    
    # If no date range, get data by time period
    return get_stock_data_by_period(stock_symbol, time_period)

@mcp.tool()
def analyze_sentiment(text: str) -> str:
    """
    Analyzes the sentiment of financial or stock-related text using a language model (LLM) via Ollama.

    This tool uses a fine-tuned LLM (e.g., LLaMA 3.2 via Ollama) to classify the sentiment of a 
    given input text as Positive, Negative, or Neutral. It is designed specifically for financial 
    contexts, including stock news, earnings reports, or market commentary.

    The tool returns a structured response that includes:
      - Sentiment classification (Positive, Negative, or Neutral)
      - A concise explanation supporting the sentiment decision

    Args:
        text (str): The financial or stock-related input text to analyze.

    Returns:
        str: A structured string containing the sentiment classification and a brief reasoning.

    Note:
        This function is optimized for finance-specific language and may not generalize well to
        other domains or non-financial sentiment analysis tasks.
    """
    return get_sentiment_analysis(text)

@mcp.tool()
def track_market_trends(stock_symbol: str) -> str:
    """ 
    Tracks and provides a market trend for a given stock symbol by querying DuckDuckGo and summarizing using Ollama.
    
    Arguments:
        stock_symbol (str): The stock symbol to fetch market trends for.

    Returns:
        str: A simulated market trend summary.
    """
    return get_market_trends(stock_symbol)

@mcp.tool()
def financial_advisor(stock_symbol: str) -> str:
    """ 
    Provides financial advice based on stock symbol by fetching stock data and analyzing sentiment.
    
    Arguments:
        stock_symbol (str): The stock symbol to provide financial advice for.

    Returns:
        str: Simulated financial advice based on data and sentiment analysis.
    """
    return get_financial_advisor(stock_symbol)

# Start the MCP server and make it ready to accept requests
if __name__ == "__main__":
    mcp.run()