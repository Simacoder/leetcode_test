# using merge sort for better efficiency with O(N log N) linearithmic time
def merge(arr, left, mid, right):
    # create temp arrays
    L = arr[left: mid + 1]
    R = arr[mid + 1: right + 1]

    i = j = 0
    k = left

    # merge the process
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

        # Copy any remaining elements
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

        # Copy any remianing elements
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)
        merge(arr, left, mid, right)



# Test Code
arr = [13, 46, 24, 52, 20, 9]
mergeSort(arr, 0, len(arr) - 1)
print(*arr)
