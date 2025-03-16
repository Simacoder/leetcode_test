# Two sum solution
def twoSum(nums, target):
    prevMap = {} # hash buckets val : index
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return[prevMap[diff], i]
        prevMap[n] = i
    return


# test code
nums = [2, 1, 5, 3]
target = 4
print(twoSum(nums, target))