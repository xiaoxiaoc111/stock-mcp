from fastapi import FastAPI, Request
import requests

app = FastAPI()

# 原始股票查询接口
@app.post("/stock")
async def stock_handler(request: Request):
    body = await request.json()
    messages = body.get("messages", [])
    if not messages:
        return {"error": "No messages provided"}
    user_message = messages[-1].get("content", "")
    # 模拟返回结果（你可以替换为真实逻辑）
    return {"stock": "TSLA", "query": user_message, "price": 250.0}

# 代理接口，转发到 /stock
@app.post("/proxy")
async def proxy_handler(request: Request):
    body = await request.json()
    messages = body.get("messages", [])
    if not messages:
        return {"error": "No messages provided"}
    user_message = messages[-1].get("content", "")

    payload = {
        "model": "stock-mcp",
        "messages": [{"role": "user", "content": user_message}]
    }

    # 转发到本服务的 /stock 路径
    response = requests.post("http://127.0.0.1:8000/stock", json=payload)
    return response.json()

# 健康检查
@app.get("/")
def health():
    return {"status": "ok"}
