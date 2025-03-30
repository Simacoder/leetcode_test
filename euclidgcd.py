# efficient algorithm for finding the greatest common divisor
def euclidgcd(a, b):
    if b == 0:
        return a
        
    return euclidgcd(b, a % b)

# test code
n = int(input('Enter the number: '))
m = int(input("Enter the number: "))
result = euclidgcd(n, m)
print(f"The GCD of {n} and {m} is: {result}")