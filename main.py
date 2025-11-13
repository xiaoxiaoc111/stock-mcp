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
    messages = body.get("messages", [])
    if not messages:
        return {"error": "No messages provided"}
    
    user_message = messages[-1].get("content", "")
    symbol = user_message.split()[0].upper()  # 简单提取股票代码
    
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json().get("Global Quote", {})
    
    return {
        "symbol": symbol,
        "price": data.get("05. price", "N/A"),
        "change": data.get("09. change", "N/A"),
        "percent": data.get("10. change percent", "N/A")
    }
