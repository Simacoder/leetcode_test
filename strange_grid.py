"""
    A strange grid has been recovered from an old book. It has  columns and infinite number of rows.
    The bottom row is considered as the first row. First few rows of the grid are like this:
    ..............

..............

20 22 24 26 28

11 13 15 17 19

10 12 14 16 18

 1  3  5  7  9

 0  2  4  6  8

"""
def strange_grid(r, c):
    """
    The function takes two integers r and c as input, representing the row and column of the grid.
    It returns the value at that position in the grid.
    """
    base = ((r -1 ) // 2) * 10
    # if r is even, add 1 to the base
    if r % 2 == 0:
        base += 1

    # column offset: increase by 2 each column
    value = base + (c - 1) * 2
    return value
    

# Test code
r, c = map(int, input().split())
print(strange_grid(r, c))