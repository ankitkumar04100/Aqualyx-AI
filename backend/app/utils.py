def classify_risk(probability: float) -> str:
    if probability < 0.3:
        return "Normal"
    elif probability < 0.7:
        return "Warning"
    return "Critical"


def calculate_savings(probability: float, usage: float):
    if probability < 0.7:
        return 0, 0, 0

    water_saved = usage * 0.4
    cost_saved = water_saved * 0.002  # Example cost per liter
    environmental_score = water_saved * 0.1

    return water_saved, cost_saved, environmental_score
