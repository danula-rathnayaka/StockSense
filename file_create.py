import os
import subprocess

folders = [
    "mcp_servers",
    "langchain_chains",
    "data/news",
    "data/stock",
    "data/reports",
    "utils"
]

files = {
    "main.py": '''\
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
''',

    "README.md": "# StockSense\nReal-time stock market sentiment, news, and trend analysis powered by MCP agents and LangChain.",

    "requirements.txt": "langchain\nfastapi\nmcp\nopenai\nrequests\n",

    ".env": "# Place your API keys here\n",

    "mcp_servers/__init__.py": "",
    "langchain_chains/__init__.py": "",
    "utils/__init__.py": "",

    "mcp_servers/news_aggregator.py": "def register(mcp):\n    pass\n",
    "mcp_servers/stock_data.py": "def register(mcp):\n    pass\n",
    "mcp_servers/research_fetcher.py": "def register(mcp):\n    pass\n",
    "mcp_servers/sentiment_analyzer.py": "def register(mcp):\n    pass\n",
    "mcp_servers/trend_watcher.py": "def register(mcp):\n    pass\n",

    "langchain_chains/sentiment_chain.py": "# LangChain chain for sentiment\n",
    "langchain_chains/synthesis_chain.py": "# LangChain chain for synthesis\n",
    "langchain_chains/recommendation_chain.py": "# LangChain chain for trading recommendation\n",

    "utils/logger.py": "import logging\nlogging.basicConfig(level=logging.INFO)\nlogger = logging.getLogger('stocksense')\n",
    "utils/config.py": "# Load .env config here\n",
    "utils/formatters.py": "# Text formatting utils\n",
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for path, content in files.items():
    with open(path, "w") as f:
        f.write(content)

# Initialize Git if not already initialized
if not os.path.exists(".git"):
    subprocess.run(["git", "init"])
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "Initial commit for StockSense"])
    print("✅ Git repo initialized and initial commit created.")
else:
    print("🔁 Git repo already exists. Skipping Git init.")

print("✅ Project structure created.")
print("📌 Now run: git remote add origin <your_repo_url> && git push -u origin main")
