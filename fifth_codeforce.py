# sales problem of Bob
# for easy to follow 
"""
Bob is a salesperson who earns a base salary of $500 per week 
plus a 7% commission on his total sales for that week. 
Write a Python program that prompts the user to enter Bob's 
total sales for the week and then calculates and displays his total earnings 
for that week.Once Bob got to a sale of old TV sets. 
There were n TV sets at that sale. TV set with index i costs ai bellars.
 Some TV sets have a negative price — their owners are ready to pay Bob if 
 he buys their useless apparatus. Bob can «buy» any TV sets he wants.
 Though he's very strong, Bob can carry at most m TV sets, and 
 he has no desire to go to the sale for the second time.
 Please, help Bob find out the maximum sum of money that he can earn.
"""

# reading the input values
n, m = map(int, input().split())
a = list(map(int, input().split()))

# first take all the negative  prices
negative_prices = [price for price in a if price < 0]
#sorting in ascending order

negative_prices.sort()

# take at most m items and sum their absolute values
max_earnings = -sum(negative_prices[:m])

print(max_earnings)
