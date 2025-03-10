from flask import Flask, request, jsonify
import librosa
import numpy as np
import joblib
import os
from audio_processing import extract_features
from model import load_model, predict_depression

app = Flask(__name__)
MODEL_PATH = "depression_model.pkl"
model = load_model(MODEL_PATH)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload_audio():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    features = extract_features(filepath)
    prediction, accuracy = predict_depression(model, features)

    return jsonify({
        "prediction": "Depressed" if prediction == 1 else "Not Depressed",
        "accuracy": accuracy
    })

if __name__ == "__main__":
    app.run(debug=True)
