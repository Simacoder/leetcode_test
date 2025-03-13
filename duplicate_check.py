# creates the function 
def contain_dup(nums):
    # creates empty set
    my_set = set()
    # Loop through the array
    for n in nums:
        # checks if it is in the set if not add
        if n in my_set:
            return True
        
        my_set.add(n)
    return False

# Test Code
nums = [1 , 2 , 3, 4, 5]
results = contain_dup(nums)
print(results)