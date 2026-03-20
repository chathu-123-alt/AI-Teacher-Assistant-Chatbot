import pickle
import os

def load_model():
    base_path = os.path.dirname(os.path.dirname(__file__))  
    model_path = os.path.join(base_path, "model", "model.pkl")

    with open(model_path, "rb") as f:
        return pickle.load(f)

model = load_model()

def predict_score(features):
    prediction = model.predict([features])
    return prediction[0]