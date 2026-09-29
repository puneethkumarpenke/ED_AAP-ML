import shap
import numpy as np

def explain(model, features):
    explainer = shap.Explainer(model)
    shap_values = explainer(np.array([features]))

    importance = {
        "Hemoglobin": abs(shap_values.values[0][0]),
        "RBC": abs(shap_values.values[0][1]),
        "MCV": abs(shap_values.values[0][2]),
        "Age": abs(shap_values.values[0][3]),
        "Gender": abs(shap_values.values[0][4])
    }

    total = sum(importance.values())
    for k in importance:
        importance[k] = round((importance[k]/total)*100, 2)

    return importance
def explanation_valid(exp):
    if exp["Hemoglobin"] < max(exp.values()):
        return False
    if (exp["Age"] + exp["Gender"]) > (exp["MCV"] + exp["RBC"]):
        return False
    return True
import pandas as pd

def stability_check(current_features):
    history = pd.read_csv("data/patient_history.csv")

    if history.empty:
        return 1.0

    stable = 0
    for _, row in history.iterrows():
        if row["top_feature"] == current_features[0]:
            stable += 1

    return stable / len(history)
