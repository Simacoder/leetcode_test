# Garden Optimizer for University Cup 2024

import json
from itertools import combinations, product
from random import sample, choice, seed
from math import dist

seed(42)  # For reproducibility

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

# Herb Data
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
    "Cilantro": [
        {"sun": 70, "water": 30, "growth": 5},
        {"sun": 80, "water": 50, "growth": 8},
        {"sun": 100, "water": 70, "growth": 11}
    ]
}

herb_prices = {"Basil": 5, "Rosemary": 7, "Cilantro": 6}

# === Functions ===
def find_valid_triangles():
    valid = set()
    for a in adjacency:
        neighbors = adjacency[a]
        for b, c in combinations(neighbors, 2):
            if c in adjacency[str(b)] and a in adjacency[str(c)]:
                triangle = tuple(sorted([int(a), int(b), int(c)]))
                valid.add(triangle)
    return list(valid)

def nearest_condition(conditions, actual_sun, actual_water):
    distances = [(abs(c["sun"] - actual_sun) + abs(c["water"] - actual_water), i) for i, c in enumerate(conditions)]
    distances.sort()
    return distances[0][1] if distances[0][0] != distances[1][0] else min(distances[0][1], distances[1][1])

def compute_sunlight(index, all_herbs):
    x1, y1 = hex_coords[str(index)]
    shade = 0
    for i, _ in all_herbs:
        if i == index:
            continue
        x2, y2 = hex_coords[str(i)]
        if y2 < y1 and abs(x2 - x1) <= 1:
            shade += 20  # Simplified
    return max(100 - shade, 0)

def compute_water(index, sprinklers):
    water = 0
    for s in sprinklers:
        if index in s:
            water += 40
        elif any(n in s for n in adjacency[str(index)]):
            water += 20
    return min(water, 100)

def compute_total_profit(herb_list, sprinkler_list):
    total = 0
    type_counts = {}
    for index, herb in herb_list:
        sunlight = compute_sunlight(index, herb_list)
        water = compute_water(index, sprinkler_list)
        condition_idx = nearest_condition(herbs[herb], sunlight, water)
        growth = herbs[herb][condition_idx]["growth"]
        profit = growth * 10 * herb_prices[herb]
        total += profit
        type_counts[herb] = type_counts.get(herb, 0) + 1

    for herb, count in type_counts.items():
        total_herbs = sum(type_counts.values())
        p = count / total_herbs * 100
        if p > 50:
            penalty = total / 2 + p
            total = total - penalty
    return total

def optimize_garden():
    best_profit = 0
    best_layout = {}
    valid_triangles = find_valid_triangles()
    all_indices = list(map(int, hex_coords.keys()))

    for _ in range(200):
        herb_spots = sample(all_indices, 6)
        herb_choices = [(i, choice(list(herbs.keys()))) for i in herb_spots]
        sprinkler_choices = sample(valid_triangles, min(3, len(valid_triangles)))
        profit = compute_total_profit(herb_choices, sprinkler_choices)

        if profit > best_profit:
            best_profit = profit
            best_layout = {
                "Herbs": [[i, h] for i, h in herb_choices],
                "Sprinklers": [list(t) for t in sprinkler_choices]
            }
    return best_profit, best_layout

if __name__ == "__main__":
    score, layout = optimize_garden()
    print("Best Profit:", round(score, 2))
    print(json.dumps(layout, indent=2))
