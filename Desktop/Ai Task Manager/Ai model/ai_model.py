from flask import Flask, request, jsonify
from transformers import pipeline

ai_app = Flask(__name__)  # Renamed app to ai_app
sentiment_model = pipeline("sentiment-analysis")

@ai_app.route("/analyze", methods=["POST"])
def analyze():
    text = request.json["text"]
    sentiment = sentiment_model(text)
    return jsonify(sentiment)

if __name__ == "__main__":
    ai_app.run(port=5001)

