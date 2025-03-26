# Quadratic time of Big O
colors = ['yellow', 'green', 'blue']

def quadratic(colors):
    for first in colors:
        for second in colors:
            print(first, second)

# test code
quadratic(colors)
