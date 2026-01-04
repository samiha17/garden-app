# Get user input instead of hardcoded values
season = input("Enter the current season (summer/winter): ").lower()
plant_type = input("Enter the plant type (flower/vegetable): ").lower()

# Variable to hold gardening advice
advice = ""

# Dictionaries to store gardening advice
SEASON_ADVICE = {
    "summer": "Water your plants regularly and provide some shade.\n",
    "winter": "Protect your plants from frost with covers.\n",
}

PLANT_ADVICE = {
    "flower": "Use fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests!",
}


def get_gardening_advice(season, plant_type):
    """
    Returns gardening advice based on season and plant type.

    :param season: str
    :param plant_type: str
    :return: str
    """
    advice = ""
    advice += SEASON_ADVICE.get(season, "No advice for this season.\n")
    advice += PLANT_ADVICE.get(plant_type, "No advice for this type of plant.")
    return advice


# Generate and print advice
print(get_gardening_advice(season, plant_type))
