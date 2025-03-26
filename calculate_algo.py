# Calculating the Big O
colors = ['green', 'blue', 'grey', 'yellow']
other_colors = ['black', 'white']
def complex_algorithm(colors):
    color_count = 0
    for color in colors:
        print(color)
        color_count += 1

    for other_color in other_colors:
        print(other_color)
        color_count += 1

    print(color_count)
complex_algorithm(colors)
