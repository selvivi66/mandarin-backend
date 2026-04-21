from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "API is running"

@app.route("/analyze", methods=["POST"])
def analyze():
    return jsonify({
        "message": "analyze endpoint works"
    })