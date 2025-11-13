from fastapi import FastAPI, Request
import requests

app = FastAPI()

STOCK_API_URL = "https://web-production-b3730.up.railway.app/stock"

@app.get("/")
def health():
    return {"status": "proxy-ok"}

@app.post("/proxy")
async def proxy_handler(request: Request):
    body = await request.json()
    # 提取 Chatbox 风格的请求内容
    messages = body.get("messages", [])
    if not messages:
        return {"error": "No messages provided"}
    
    user_message = messages[-1].get("content", "")
    
    # 构造转发请求体
    payload = {
        "model": "stock-mcp",
        "messages": [
            {"role": "user", "content": user_message}
        ]
    }

    # 转发 POST 请求到原始 /stock 接口
    response = requests.post(STOCK_API_URL, json=payload)
    return response.json()
