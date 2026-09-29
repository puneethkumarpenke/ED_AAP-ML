import joblib

logistic_model = joblib.load("models/logistic_model.pkl")
rf_model = joblib.load("models/rf_model.pkl")
xgb_model = joblib.load("models/xgb_model.pkl")

def predict(model, features):
    prediction = model.predict([features])[0]
    confidence = max(model.predict_proba([features])[0])
    return prediction, confidence
