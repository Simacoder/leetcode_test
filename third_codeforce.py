# greed challenge jafar has 2 can of cola each can describe by 2 integer 

# reading the input 
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# define the total
total = sum(a)
# sort the list
b.sort(reverse=True)

if b[0] + b[1] >= total:
    print("YES")
else:
    print("NO")
