from fastapi import FastAPI, Request
import requests

app = FastAPI()

STOCK_API_URL = "https://web-production-b3730.up.railway.app/stock"

@app.post("/proxy")
async def proxy_handler(request: Request):
    body = await request.json()
    messages = body.get("messages", [])
    if not messages:
        return {"error": "No messages provided"}
    
    user_message = messages[-1].get("content", "")
    
    payload = {
        "model": "stock-mcp",
        "messages": [
            {"role": "user", "content": user_message}
        ]
    }

    response = requests.post(STOCK_API_URL, json=payload)
    return response.json()
