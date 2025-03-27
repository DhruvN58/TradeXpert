import requests
import os

MARKET_API_URL = "https://www.alphavantage.co/query"
API_KEY = os.getenv("MARKET_API_KEY", "GA84WDXY9TBOAYTY")  # Use environment variable

def get_market_data(symbol: str):
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": "5min",
        "apikey": API_KEY,
    }
    response = requests.get(MARKET_API_URL, params=params)
    return response.json()
