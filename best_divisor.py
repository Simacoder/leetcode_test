"""
    Kristen loves playing with and comparing numbers. She thinks that if she takes two different positive numbers, the one whose digits sum to a larger number is better than the other. If the sum of digits is equal for both numbers, then she thinks the smaller number is better. For example, Kristen thinks that  is better than  and that  is better than .

Given an integer, , can you find the divisor of  that Kristin will consider to be the best?

Input Format

A single integer denoting .

Constraints

Output Format

Print an integer denoting the best divisor of .

"""

import math
import os
import random
import re
import sys

def sum_digit(number):
    """
    Returns the sum of digits of a number.
    """
    return sum([int(i) for i in str(number)])

def best_divisor(n):
    best_div = 1
    max_best_sum = 1

    for i in range(1, int(n**0.5)+ 1):
        if n % i == 0:
            # check if i is a better divisor
            for divisor in (i, n// i):
                current_digit_sum = sum_digit(divisor)
                if (current_digit_sum > max_best_sum or \
                    (current_digit_sum == max_best_sum and divisor < best_div)):
                    best_div = divisor
                    max_best_sum = current_digit_sum
    return best_div


# test code
if __name__ == '__main__':
    n = int(input("Ente your number").strip())
    result = best_divisor(n)
    print(result)

