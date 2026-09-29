# models.py
import numpy as np

def logistic_regression_predict(features: dict):
    hb = features["hemoglobin"]
    risk = max(0.0, min(1.0, (13 - hb) / 6))
    prediction = "Anaemia" if risk > 0.5 else "No Anaemia"
    confidence = float(0.7 + 0.3 * risk)
    return prediction, confidence

def random_forest_predict(features: dict):
    hb = features["hemoglobin"]
    mcv = features["mcv"]
    risk = max(0.0, min(1.0, (13 - hb) / 5 + (80 - mcv) / 60))
    prediction = "Anaemia" if risk > 0.5 else "No Anaemia"
    confidence = float(0.75 + 0.25 * risk)
    return prediction, confidence

def xgboost_predict(features: dict):
    hb = features["hemoglobin"]
    mch = features["mch"]
    risk = max(0.0, min(1.0, (13 - hb) / 5 + (27 - mch) / 20))
    prediction = "Anaemia" if risk > 0.5 else "No Anaemia"
    confidence = float(0.72 + 0.28 * risk)
    return prediction, confidence

def explain_features(model_name: str, features: dict):
    hb = features["hemoglobin"]
    mcv = features["mcv"]
    rbc = features["rbc"]
    age = features["age"]

    hb_score  = abs(13 - hb)
    mcv_score = abs(90 - mcv)
    rbc_score = abs(4.5 - rbc)
    age_score = age / 80

    scores = {
        "Hemoglobin": hb_score,
        "MCV": mcv_score,
        "RBC": rbc_score,
        "Age": age_score,
        "Gender": 0.2
    }

    total = sum(scores.values()) or 1
    importance = {k: round(v / total * 100, 2) for k, v in scores.items()}
    importance_sorted = dict(sorted(importance.items(), key=lambda x: x[1], reverse=True))
    return importance_sorted