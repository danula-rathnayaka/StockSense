from mcp.server.fastmcp import FastMCP

from langchain_chains.news_chain import get_news_analysis as get_news_analysis_chain
from langchain_chains.stock_data import get_stock_data_by_dates, get_stock_data_by_period
# Create an MCP server instance
mcp = FastMCP("StockSense")

# Registering news aggregator tool with a basic string processing
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

# Registering stock data tool with a basic calculation
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

# Registering research fetcher tool with simple word count
@mcp.tool()
def fetch_research_papers(stock_symbol: str) -> str:
    """
    Simulating fetching research papers by counting the number of characters in the stock symbol.
    """
    return f"Research paper placeholder: {stock_symbol} has {len(stock_symbol)} characters"

# Registering sentiment analyzer tool with simple text analysis
@mcp.tool()
def analyze_sentiment(text: str) -> str:
    """
    Simulating sentiment analysis by counting the vowels in the input text.
    """
    vowels = "AEIOUaeiou"
    vowel_count = sum(1 for char in text if char in vowels)
    return f"Sentiment analysis placeholder: {vowel_count} vowels found in '{text}'"

# Registering trend watcher tool with string manipulation
@mcp.tool()
def track_market_trends(stock_symbol: str) -> str:
    """
    Simulating trend tracking by returning the stock symbol in uppercase.
    """
    return f"Market trend for {stock_symbol}: {stock_symbol.upper()}"

# Start the MCP server and make it ready to accept requests
if __name__ == "__main__":
    mcp.run(transport="STDIO") #  transport = SSE | STDIO