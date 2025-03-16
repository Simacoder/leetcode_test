# for simplicity and learning using a brute force solution to make it easy to understand 
def two_sum(nums, target):
    # nested or loop that runs for O(n^2) for is much more slow  compare to hashMap function (O(n)
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return[i, j]
            
# test code
nums = [2, 1, 5, 3]
target = 4
print(two_sum(nums, target))