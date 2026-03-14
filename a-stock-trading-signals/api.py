"""
统一API - 支持所有3个交易信号
"""
from fastapi import FastAPI
app = FastAPI(title="A股交易信号API")

VCP_SIGNALS = [
    {"code": "688041", "name": "纳芯微", "price": 125.80, "change": 4.5, "sector": "半导体", "rvol": 2.3, "stars": "⭐⭐⭐", "stop_loss": 119.51, "target": 138.38},
    {"code": "688126", "name": "沪硅产业", "price": 28.90, "change": 3.2, "sector": "半导体", "rvol": 1.8, "stars": "⭐⭐", "stop_loss": 27.46, "target": 31.79},
]
N_SIGNALS = [
    {"code": "000858", "name": "五粮液", "price": 158.60, "change": 4.2, "stage": "再次启动", "stars": "⭐⭐⭐", "stop_loss": 150.67, "target": 174.46},
    {"code": "601318", "name": "中国平安", "price": 48.50, "change": 3.5, "stage": "突破", "stars": "⭐⭐", "stop_loss": 46.08, "target": 53.35},
]
SIGNALS = [
    {"code": "300750", "name": "宁德时代", "price": 285.50, "change": 5.2, "inflow": "2.5亿", "stars": "⭐⭐⭐", "stop_loss": 271.23, "target": 314.05},
    {"code": "002594", "name": "比亚迪", "price": 268.80, "change": 3.8, "inflow": "1.8亿", "stars": "⭐⭐", "stop_loss": 255.36, "target": 295.68},
]
PAYMENT = {"price": "0.01 USDC", "wallet": "0x1a9275EE18488A20C7898C666484081F74Ee10CA", "chain": "Base"}

@app.get("/")
def root(): return {"message": "A股交易信号API", "endpoints": ["/signals", "/vcp", "/n-pattern"], "payment": PAYMENT}
@app.get("/signals")
def get_signals(): return {"success": True, "pattern": "旱地拔葱", "signals": SIGNALS, "payment": PAYMENT}
@app.get("/vcp")
def get_vcp(): return {"success": True, "pattern": "VCP", "signals": VCP_SIGNALS, "payment": PAYMENT}
@app.get("/n-pattern")
def get_n_pattern(): return {"success": True, "pattern": "N字型态", "signals": N_SIGNALS, "payment": PAYMENT}
