app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():