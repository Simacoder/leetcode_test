import json
from itertools import combinations
from math import fabs

# === Garden Layout ===
hex_coords = {
    "0": [0, 0], "1": [0, 2], "2": [0, 4], "3": [0, 6],
    "4": [0, 1], "5": [0, 3], "6": [0, 5], "7": [1, 2],
    "8": [1, 4], "9": [1, 1], "10": [1, 3], "11": [1, 5],
    "12": [2, 2], "13": [2, 4], "14": [2, 3], "15": [3, 2],
    "16": [3, 4], "17": [3, 3], "18": [4, 3]
}

adjacency = {
    "0": [4], "1": [4, 5, 7], "2": [5, 6, 8], "3": [6],
    "4": [0, 1, 7, 9], "5": [1, 2, 7, 8, 10], "6": [2, 3, 8, 11],
    "7": [1, 4, 5, 9, 10, 12], "8": [2, 5, 6, 10, 11, 13],
    "9": [4, 7, 12], "10": [5, 7, 8, 12, 13, 14],
    "11": [6, 8, 13], "12": [7, 9, 10, 14, 15],
    "13": [8, 10, 11, 14, 16], "14": [10, 12, 13, 15, 16, 17],
    "15": [12, 14, 17], "16": [13, 14, 17], "17": [14, 15, 16, 18],
    "18": [17]
}

# === Herb Data ===
herbs = {
    "Basil": [
        {"sun": 40, "water": 60, "growth": 2},
        {"sun": 60, "water": 70, "growth": 5},
        {"sun": 90, "water": 80, "growth": 8}
    ],
    "Rosemary": [
        {"sun": 60, "water": 50, "growth": 4},
        {"sun": 70, "water": 60, "growth": 7},
        {"sun": 100, "water": 80, "growth": 10}
    ],
    # Add others similarly...
}

herb_prices = {
    "Basil": 5,
    "Rosemary": 7,
    # Add others...
}

# === Example Setup ===
herb_placement = [(10, "Rosemary"), (5, "Basil")]
sprinklers = [(10, 12, 14)]  # Placeholder: should check validity

# === Utilities ===
def nearest_condition(conditions, actual_sun, actual_water):
    distances = []
    for i, cond in enumerate(conditions):
        dist = abs(cond["sun"] - actual_sun) + abs(cond["water"] - actual_water)
        distances.append((dist, i))
    distances.sort()
    best_index = distances[0][1]
    # Downgrade if tie
    if len(distances) > 1 and distances[0][0] == distances[1][0]:
        best_index = min(distances[0][1], distances[1][1])
    return best_index

# === Dummy Computation ===
def compute_profit():
    total = 0
    for index, name in herb_placement:
        # Simulate perfect 100% sunlight and water
        sunlight = 100
        water = 80
        conditions = herbs[name]
        cond_index = nearest_condition(conditions, sunlight, water)
        growth = conditions[cond_index]["growth"]
        profit = growth * 10 * herb_prices[name]
        total += profit
    return total

# === Output ===
garden_json = {
    "Herbs": [[i, h] for i, h in herb_placement],
    "Sprinklers": [list(s) for s in sprinklers]
}

print("Estimated Profit:R", compute_profit())
print(json.dumps(garden_json, indent=2))
