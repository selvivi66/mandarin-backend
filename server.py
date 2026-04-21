from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "API is live"

@app.route("/analyze", methods=["POST"])
def analyze():
    if "audio" not in request.files:
        return jsonify({"error": "No audio uploaded"}), 400

    return jsonify({
        "transcription": "你好",
        "pinyin": "nǐ hǎo",
        "correction": "Tone 3 needs deeper dip",
        "tts_url": "https://example.com/audio.mp3"
    })