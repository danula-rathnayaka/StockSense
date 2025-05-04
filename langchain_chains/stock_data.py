import yfinance as yf

def get_stock_data_by_period(ticker: str, time_period: str) -> str:
    """
    Fetch stock data for a given time period (like "1d", "1mo", "1y").
    
    Args:
        ticker: The ticker symbol of the stock.
        time_period: The time period to get the stock data for. 
                      (1d, 5d, 1mo, 3mo, 6mo, 1y, 5y, 10y, ytd, max)
    
    Returns:
        A string containing all stock data for the given time period.
    """
    data = yf.Ticker(ticker)
    stock_data = data.history(period=time_period)

    if stock_data.empty:
        return f"No data available for ticker {ticker} with the time period {time_period}"
    
    return str(stock_data)

def get_stock_data_by_dates(ticker: str, start_date: str, end_date: str) -> str:
    """
    Fetch stock data between a specific date range.
    
    Args:
        ticker: The ticker symbol of the stock.
        start_date: The start date in 'YYYY-MM-DD' format.
        end_date: The end date in 'YYYY-MM-DD' format.
    
    Returns:
        A string containing all stock data for the given date range.
    """
    data = yf.Ticker(ticker)
    stock_data = data.history(start=start_date, end=end_date)

    if stock_data.empty:
        return f"No data available for ticker {ticker} between {start_date} and {end_date}"
    
    return str(stock_data)