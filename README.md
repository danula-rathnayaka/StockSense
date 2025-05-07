# StockSense MCP Server

StockSense is an MCP (Model Context Protocol) server designed to provide various financial and stock-related tools and services. MCP servers enable communication between different services in a distributed system, making it easy to create and scale applications that handle specific tasks. In this project, StockSense integrates multiple services such as stock data retrieval, sentiment analysis, news analysis, and market trend tracking to assist with financial decision-making.

By using the MCP architecture, StockSense leverages efficient communication between tools for seamless functionality.

---

## MCP Server

MCP (Model Context Protocol) is a lightweight server framework designed to enable tool-based microservices. Each tool in the system performs a specific function, and the MCP server facilitates communication between them. This architecture is ideal for building modular applications, allowing each service to be developed, deployed, and maintained independently.

In StockSense, the MCP server hosts several tools related to financial services and allows them to interact efficiently. Tools are registered with the server and made accessible via specific function calls. The server can be expanded with additional tools to provide more capabilities as needed.

---

## Architecture Diagram

Below is the architecture diagram of the **StockSense MCP Server**:

![MCP Server Architecture](./mcp-server-architecture.png)

---

## Tools

StockSense provides the following tools to assist with stock analysis and financial advice:

1. **`get_news(stock_symbol: str)`** - Fetches news for a given stock symbol using DuckDuckGo.
2. **`get_stock_data(stock_symbol: str, time_period: str = "1y", start_date: str = None, end_date: str = None)`** - Stock data retrieval based on the symbol and optional time period or date range using yfinance.
3. **`analyze_sentiment(text: str)`** - Analyzes sentiment of financial or stock-related text using a language model (LLM) via Ollama.

4. **`track_market_trends(stock_symbol: str)`** - Tracks market trends by querying DuckDuckGo and summarizing trends using Ollama.

5. **`financial_advisor(stock_symbol: str)`** - Provides financial advice based on stock data, news, and sentiment analysis.
