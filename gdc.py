# find the greatetst common divisor
def naivegcd(a, b):
    best = 0
    for d in range(1, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            best = d
    return best

# test code
n = int(input("Enter the number: "))
m = int(input("Entee the number: "))
result = naivegcd(n,m)
print(f"GCD of {n} and {m} is: {result}") 