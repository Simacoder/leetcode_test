# selection sorting algorithm 

def selection_sort(arr, N):
    for i in range(N - 1): # loop through each element
        min_index = i # Assumed the element has smallest value
        for j in range(i + 1, N):
            if arr[j] < arr[min_index]: 
                min_index = j
            # Swap the indices to find the min element 
        arr[i], arr[min_index] = arr[min_index], arr[i]


# Test code
N = 6
arr = [13, 46, 24, 52, 20, 3]
selection_sort(arr, N)
print(*arr)

