from flask import Flask, jsonify

app = Flask(__name__)

# 数据定义
P = {"price": "0.01 USDC", "w": "0x1a9275EE18488A20C7898C666484081F74Ee10CA"}
S = [{"c": "300750", "n": "宁德时代", "p": 285.5, "ch": 5.2}]
V = [{"c": "688041", "n": "纳芯微", "p": 125.8, "ch": 4.5}]
N = [{"c": "000858", "n": "五粮液", "p": 158.6, "ch": 4.2}]

@app.route('/')
def h():
    return jsonify({"e": ["/s", "/v", "/n"], "p": P})

@app.route('/s')
def get_s():
    return jsonify({"s": S, "p": P})

@app.route('/v')
def get_v():
    return jsonify({"s": V, "p": P})

@app.route('/n')
def get_n():
    return jsonify({"s": N, "p": P})

# 必须包含这一行，Vercel 才能识别 Flask 实例
app = app
