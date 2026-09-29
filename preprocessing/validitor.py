def validate_input(data):
    if data["hemoglobin"] <= 0:
        return False, "Invalid hemoglobin"

    if not (60 <= data["mcv"] <= 110):
        return False, "MCV out of range"

    if data["rbc"] <= 2:
        return False, "Invalid RBC"

    return True, "Valid input"
