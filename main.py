from fastapi import FastAPI, Request
from stock_logic import fetch_stock_price, format_markdown_table, risk_analysis

app = FastAPI()

@app.post("/stock")
async def stock_handler(request: Request):
    body = await request.json()
    messages = body.get("messages", [])
    user_message = messages[-1].get("content", "")
    
    # 支持多股查询：TSLA, AAPL, NVDA
    symbols = [s.strip().upper() for s in user_message.replace("，", ",").split(",")]
    prices = {symbol: fetch_stock_price(symbol) for symbol in symbols}
    
    markdown = format_markdown_table(prices)
    risk = risk_analysis(prices)
    
    return {
        "markdown": markdown,
        "risk": risk,
        "raw": prices
    }

@app.post("/proxy")
async def proxy_handler(request: Request):
    body = await request.json()
    messages = body.get("messages", [])
    user_message = messages[-1].get("content", "")
    
    # 构造模拟请求体转发到 /stock
    symbols = [s.strip().upper() for s in user_message.replace("，", ",").split(",")]
    prices = {symbol: fetch_stock_price(symbol) for symbol in symbols}
    
    markdown = format_markdown_table(prices)
    risk = risk_analysis(prices)
    
    return {
        "markdown": markdown,
        "risk": risk,
        "raw": prices
    }

@app.get("/")
def health():
    return {"status": "ok"}
