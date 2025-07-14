def solve_test_case(n, k, arr):
    """
    Final optimized solution for the Maximize NOR problem.
    
    The NOR operation on a subarray is equal to the bitwise NOT of the OR of all elements.
    For each position i, we find the maximum NOR value of any subarray that includes it.
    
    Time complexity: O(n²)
    Space complexity: O(n)
    """
    mask = (1 << k) - 1  # Mask to keep only k bits
    result = [0] * n
    
    # Precompute OR values for efficient calculation
    # left_or[i][j] = OR of elements from j to i (inclusive)
    left_or = [[0] * n for _ in range(n)]
    
    # Fill left_or values
    for i in range(n):
        left_or[i][i] = arr[i]
        for j in range(i-1, -1, -1):
            left_or[i][j] = left_or[i][j+1] | arr[j]
    
    # Calculate right_or on the fly
    for i in range(n):
        # Try all possible subarrays containing position i
        for left in range(i+1):
            # OR value from left to i
            or_value = left_or[i][left]
            
            # Calculate NOR of [left...i]
            nor_value = (~or_value) & mask
            result[i] = max(result[i], nor_value)
            
            # Extend to the right
            for right in range(i+1, n):
                or_value |= arr[right]
                nor_value = (~or_value) & mask
                result[i] = max(result[i], nor_value)
    
    return result

def main():
    t = int(input())
    
    for _ in range(t):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        
        result = solve_test_case(n, k, arr)
        print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()