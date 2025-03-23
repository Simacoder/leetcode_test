# recursive method
def binary_search_recursive(arr, target, left, right):
    # if the aerch cross the bounds the target is not in the array
    if left > right:
        return -1
    # calculate the middle
    mid = left + (right - left) // 2
    # if middle is eqal to target
    if arr[mid] == target:
        return mid
    #if the target is bigger then go right
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    # fi the target is smaller then go left
    else:
        return binary_search_recursive(arr, target, left, mid - 1)
    

# test the code
arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 56
result = binary_search_recursive(arr, target, 0, len(arr) - 1)
if result != - 1:
    print(f"Iterative: target found at index {result}")
else:
    print("Iterative: target is not found")