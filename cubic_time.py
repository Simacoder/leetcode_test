# doing cubic time of Big O
colors = ['blacks', 'whites', 'brown']

def cubic(colors):
    for first in colors: # O(n)
        for second in colors: # O(n)
            for third in colors: # O(n)
                print(first, second, third) # thus in total O(n^3)
cubic(colors)
