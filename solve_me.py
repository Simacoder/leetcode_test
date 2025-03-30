# this problem
# input "aaaabbbcca"
# output [("a", 4, ("b", 3), ("c", 2), ("a", 1))]

def search(n):
    if not n:
       return []
    
    result = []
    count = 1
    for i in range(1, len(n)):
       
       if n[i] == n[i - 1]:
          count += 1

       else:
          result.append((n[i - 1], count))
          count = 1
    result.append((n[-1], count))
    return result
    

# test code
my_list = "aaaabbbcca"
result = search(my_list)

print(f"{result}")
