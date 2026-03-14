from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# 收款配置
P = {
    "price": "0.01", 
    "currency": "USDC",
    "chain": "Base",
    "w": "0x1a9275EE18488A20C7898C666484081F74Ee10CA"
}

# 模拟行情数据
S = [{"c": "300750", "n": "宁德时代", "p": 285.5, "ch": 5.2}]
V = [{"c": "688041", "n": "纳芯微", "p": 125.8, "ch": 4.5}]
N = [{"c": "000858", "n": "五粮液", "p": 158.6, "ch": 4.2}]

def check_x402_payment():
    """
    检查 x402 支付状态的逻辑
    ClawHub 或 AI Agent 调用时，如果没有支付凭证，则触发 402 错误要求支付
    """
    # 获取请求头中的授权信息
    auth_header = request.headers.get('Authorization')
    
    # 如果没有授权信息（代表未支付），返回符合 x402 标准的 402 错误
    if not auth_header:
        return False
    return True

@app.route('/')
def h():
    return jsonify({
        "info": "A-Stock Signal API (x402 Protocol Active)",
        "endpoints": ["/s", "/v", "/n"],
        "pricing": P
    })

@app.route('/s')
def get_s():
    if not check_x402_payment():
        # 返回 402 状态码，ClawHub 看到这个会自动弹出支付
        response = jsonify({"error": "Payment Required", "pricing": P})
        response.headers['WWW-Authenticate'] = f'X402 price="{P["price"]}", currency="{P["currency"]}", address="{P["w"]}", chain="{P["chain"]}"'
        return response, 402
    return jsonify({"s": S, "p": P})

@app.route('/v')
def get_v():
    if not check_x402_payment():
        response = jsonify({"error": "Payment Required", "pricing": P})
        response.headers['WWW-Authenticate'] = f'X402 price="{P["price"]}", currency="{P["currency"]}", address="{P["w"]}", chain="{P["chain"]}"'
        return response, 402
    return jsonify({"s": V, "p": P})

@app.route('/n')
def get_n():
    if not check_x402_payment():
        response = jsonify({"error": "Payment Required", "pricing": P})
        response.headers['WWW-Authenticate'] = f'X402 price="{P["price"]}", currency="{P["currency"]}", address="{P["w"]}", chain="{P["chain"]}"'
        return response, 402
    return jsonify({"s": N, "p": P})

# Vercel 实例导出
app = app
