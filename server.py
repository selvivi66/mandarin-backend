from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "API is running"

@app.route("/analyze", methods=["POST"])
def analyze():
    return {"status": "ok"}   # 👈 THIS LINE FIXES YOUR ERROR