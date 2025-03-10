import joblib
import numpy as np

def load_model(model_path):
    return joblib.load(model_path)

def predict_depression(model, features):
    features = np.array(features).reshape(1, -1)
    prediction = model.predict(features)[0]
    accuracy = model.predict_proba(features).max()
    return prediction, accuracy
