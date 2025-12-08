# trippi troppi problem  the strnge world 
# input the number of texts 
t = int(input())

for _ in range(t):

    # reads the tree words
    words = input().split()
    # take the first letter of each word and join the letters
    modern_name = "".join(word[0] for word in words)
    # get =ting the the results 
    print(modern_name)