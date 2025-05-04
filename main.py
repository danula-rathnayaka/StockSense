from mcp.server.fastmcp import FastMCP

from langchain_chains.news_chain import get_news_analysis

# Create an MCP server instance
mcp = FastMCP("StockSense")

# Registering news aggregator tool with a basic string processing
@mcp.tool()
def get_news_(stock_symbol: str) -> str:
    """
    Simulates fetching news for a stock symbol by returning a placeholder analysis.
    
    This function takes a stock symbol, processes it (e.g., reverses the symbol), 
    and returns a simulated news analysis.

    Parameters:
        stock_symbol (str): The stock symbol to find information about

    Returns:
        str: A simulated news analysis
    """
    return get_news_analysis(stock_symbol)

# Registering stock data tool with a basic calculation
@mcp.tool()
def get_stock_data(stock_symbol: str) -> str:
    """
    Simulating stock data retrieval by calculating the length of the stock symbol.
    """
    return f"Stock data length for {stock_symbol}: {len(stock_symbol)}"

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
    mcp.run()
