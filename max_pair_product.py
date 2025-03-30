def max_pairwise_product(numbers):
    n = len(numbers)
    
    # Find index of the largest number
    index1 = 0
    for i in range(1, n):
        if numbers[i] > numbers[index1]:
            index1 = i

    # Find index of the second largest number (excluding index1)
    index2 = 1 if index1 == 0 else 0
    for i in range(n):
        if i != index1 and numbers[i] > numbers[index2]:
            index2 = i
    
    return numbers[index1] * numbers[index2]

# Read input
n = int(input())
numbers = list(map(int, input().split()))

# Compute and print result
print(max_pairwise_product(numbers))
