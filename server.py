from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "API is running"

@app.route("/analyze", methods=["POST"])
def analyze():
    return jsonify({
        "transcription": "测试一下",
        "pinyin": "cè shì yī xià",
        "correction": "很好，再清晰一点",
        "tone_estimate": "Tone 4 slightly off",
        "tts_url": "https://example.com/audio.mp3"
    })