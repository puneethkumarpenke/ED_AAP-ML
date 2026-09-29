def calculate_trust(confidence, explain_score, stability):
    return round(
        0.4*explain_score +
        0.4*confidence +
        0.2*stability, 3
    )
