# work on telescoping challenge hackerranker

MOD = 10**9 + 7  # Large prime number for modulo

def summingSeries(n):
    return (n * n) % MOD  # Compute n^2 % MOD
# test code
t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())  # Read each test case 
        print(summingSeries(n))  # Print the result



