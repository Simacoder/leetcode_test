def solve_test_case(n, k, arr):
    """
    Corrected solution for the Maximize NOR problem.
    
    For each position i, we find the maximum NOR value of any subarray that includes
    element at position i.
    
    Time complexity: O(n³)
    Space complexity: O(1) extra space
    """
    mask = (1 << k) - 1  # Mask to keep only k bits
    result = []
    
    for i in range(n):
        max_nor = arr[i]  # Initialize with the single element
        
        # Check all possible subarrays containing position i
        for left in range(i + 1):  # All possible left boundaries (0 to i)
            for right in range(i, n):  # All possible right boundaries (i to n-1)
                # Calculate NOR for subarray [left...right]
                nor = arr[left]
                for j in range(left + 1, right + 1):
                    nor = (~(nor | arr[j])) & mask
                
                max_nor = max(max_nor, nor)
        
        result.append(max_nor)
    
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