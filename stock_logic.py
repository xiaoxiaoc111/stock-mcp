def fetch_stock_price(symbol: str) -> float:
    # 模拟股价查询（可替换为 Alpha Vantage 或其他 API）
    mock_prices = {"TSLA": 250.0, "AAPL": 190.0, "NVDA": 480.0}
    return mock_prices.get(symbol.upper(), 0.0)

def format_markdown_table(data: dict) -> str:
    header = "| 股票代码 | 当前价格 |\n|----------|------------|\n"
    rows = "\n".join([f"| {symbol} | ${price:.2f} |" for symbol, price in data.items()])
    return header + rows

def risk_analysis(data: dict) -> str:
    tips = []
    if "TSLA" in data and data["TSLA"] > 240:
        tips.append("⚠️ TSLA 当前价格较高，注意持仓风险")
    return "\n".join(tips)
