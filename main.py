from fastapi import FastAPI, Request
import requests

app = FastAPI()
API_KEY = "UO39O45CR7OKCEOD"

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.post("/stock")
async def get_stock(request: Request):
    body = await request.json()
    symbol = body.get("symbol", "TSLA")
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json().get("Global Quote", {})
    return {
        "symbol": symbol,
        "price": data.get("05. price", "N/A"),
        "change": data.get("09. change", "N/A"),
        "percent": data.get("10. change percent", "N/A")
    }
