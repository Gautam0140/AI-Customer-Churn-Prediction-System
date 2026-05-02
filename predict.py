import joblib
import numpy as np

model = joblib.load("models/model.pkl")

def predict(input_data):
    data = np.array(input_data).reshape(1, -1)
    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]
    return prediction, probability
