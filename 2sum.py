# Two Sum 
# Given an array of integers nums and an integer target, return indices of the two numbers 
# such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the 
# same element twice.

# You can return the answer in any order.
# You can assume that each input would have exactly one solution, and you may not use the
# same element twice.
# You can return the answer in any order.
# You may not use the same element twice.
# You can return the answer in any order.
# You can assume that each input would have exactly one solution, and you may not use the
# same element twice.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
"""
# naive algorithm 
def twoSum_naive(nums, target):
    

    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums [j] == target:
                return [i, j]
    return []
"""

# optimized algorithm
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    d = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in d:
            return [d[complement], i]
        d[num] = i
  
        
# test code
if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(twoSum(nums, target)) # Output: [0, 1]
    nums = [3, 2, 4]
    target = 6
    print(twoSum(nums, target)) # Output: [1, 2]
    nums = [3, 3]
    target = 6
    print(twoSum(nums, target)) # Output: [0, 1]