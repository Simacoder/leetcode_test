# Iterative method 
def binary_search_iterative(arr, target):
    # define the search bounds
    left, right = 0, len(arr) - 1
    while left <= right:
        # calculate the middle index
        mid = (left + right) // 2
        # if middle is equal to target then return the mid
        if arr[mid] == target:
            return mid
        # if the target is bigger then go right
        elif arr[mid] < target:
            left = mid + 1
        # if the taregt is maller than the mid, go left
        else:
            right = mid - 1
    # return -1 if the raet is not found
    return -1

#test the code
arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 56
result = binary_search_iterative(arr, target)
if result != -1:
    print(f"Iterative: target found at index {result}")
else:
    print("Iterative: Target i not found")
