# IIya and the bank Account , has the issue with math

# to folow the problem
"""
Ilya the Lion has recently had a birthday, so he got a lot of gifts.
 One of them (the gift of the main ZooVille bank) is the opportunity to delete the
   last digit or the digit before last from the state of his bank account no more than once.
     For example, if the state of Ilya's bank account is -123, then Ilya can delete 
     the last digit and get his account balance equal to -12, also 
     he can remove its digit before last and get the account balance equal to -13. Of course,
 Ilya is permitted not to use the opportunity to delete a digit from the balance.

"""
# reading the input
n = int(input())

if n > 0:
    # checking for positive number , best leave as it is
    print(n)

else:
    s = str(n)

    # remove the last digit 
    option1 = int(s[: -1])
    # the option2 remove te second last digit
    option2 = int(s[: -2] + s[-1])
    # show the results
    print(max(option1, option2))