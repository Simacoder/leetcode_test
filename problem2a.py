def nor(a, b, k):
    """Compute bitwise NOR of two k-bit integers"""
    return (~(a | b)) & ((1 << k) - 1)

def solve_maximize_nor(n, k, arr):
    result = [0] * n
    
    # Precompute NOR values for each subarray
    # nor_values[l][r] will store NOR value of subarray arr[l...r]
    nor_values = [[0] * n for _ in range(n)]
    
    # Initialize with single elements
    for i in range(n):
        nor_values[i][i] = arr[i]
    
    # Compute NOR values for all subarrays
    for length in range(2, n + 1):
        for l in range(n - length + 1):
            r = l + length - 1
            nor_values[l][r] = nor(nor_values[l][r-1], arr[r], k)
    
    # Find max NOR for each index
    for i in range(n):
        max_nor_value = arr[i]  # Start with single element
        
        # Check all subarrays containing index i
        for l in range(i + 1):
            for r in range(i, n):
                max_nor_value = max(max_nor_value, nor_values[l][r])
        
        result[i] = max_nor_value
    
    return result

def main():
    t = int(input())
    
    for _ in range(t):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        
        result = solve_maximize_nor(n, k, arr)
        print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()