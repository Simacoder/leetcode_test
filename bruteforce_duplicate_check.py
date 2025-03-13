# creates a method to check the duplicate of arrays
def dup_checks(nums) -> bool:
    n = len(nums)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False

# Test code
nums = [1, 3, 2, 4, 1]
results = dup_checks(nums)
print(results)
