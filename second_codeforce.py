# Osu! mania problem the rhythm game the layout of n rows and 4 columns

# reading the input numbers to test 
t = int(input())

# rn a for looop  
for _ in range(t):

    n = int(input())

    rows = [input() for _ in range(n)]

    result = [] # empty list to store the result

    # we process from the bottom to top
    for row in reversed(rows):
        # added the new results
        result.append(row.index("#") + 1)

    # showing the results
    print(*result)
