import sys

# method for check arithmentic progression
def checkIsAp( arr, n):
    mySet = set()
    Max = -sys.maxsize - 1
    Min = sys.maxsize

    for i in arr:
        Max = max(i, Max)
        Min = min(i, Min)
        mySet.add(i)
    # Finding the common difference
    diff = (Max - Min) // (n - 1)
    count = 0

    # Check if the Arithmentic is there
    while (Max in mySet):
        count += 1
        Max = Max - diff
    
    if (count == len(arr)):
        return True
    return False

# test code
arr = [0, 12, 4, 8]
n = len(arr)
print(checkIsAp(arr, n))