from mcp.server.fastmcp import FastMCP
from mcp_servers import news_aggregator, stock_data, research_fetcher, sentiment_analyzer, trend_watcher

mcp = FastMCP("StockSense")

news_aggregator.register(mcp)
stock_data.register(mcp)
research_fetcher.register(mcp)
sentiment_analyzer.register(mcp)
trend_watcher.register(mcp)

if __name__ == "__main__":
    mcp.run()
