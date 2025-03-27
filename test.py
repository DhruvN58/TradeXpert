from fastapi import FastAPI
import requests

app = FastAPI()

# Free market data API (Example: Alpha Vantage or Yahoo Finance)
MARKET_API_URL = "https://www.alphavantage.co/query"
API_KEY = "GA84WDXY9TBOAYTY"

@app.get("/market-data/{symbol}")
def get_market_data(symbol: str):
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": "5min",
        "apikey": API_KEY,
    }
    response = requests.get(MARKET_API_URL, params=params)
    return response.json()

@app.get("/trade-signal")
def generate_trade_signal():
    """Placeholder for AI-based trade signal logic."""
    return {"signal": "BUY", "confidence": 0.85}

@app.post("/execute-trade")
def execute_trade(symbol: str, action: str, quantity: int):
    """Paper trade execution (simulated)."""
    return {"status": "executed", "symbol": symbol, "action": action, "quantity": quantity}

@app.get("/test")
async def test():
    return {"message": "Test endpoint works!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
