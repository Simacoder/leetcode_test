# Queues data structure 
from collections import deque

orders = deque()

orders.append("Burgers")
orders.append("papa and nyama")
orders.append("fries")

print(orders)

orders.popleft()
print('after removing first order')
print(orders)

# Stacks operations 
actions = deque()

actions.append("Palesa")
actions.append("Nthabiseng")
actions.append("Thato")

print(actions)
# to retrieve and remove the list we use pop()
print('after removing the last order')
actions.pop()
print(actions)

# Non linear data structures 

# hash 
hash("data")
print(hash("data") % 100)

# words
word_definition = {}
word_definition["data"] = "Facts or information."

print(word_definition["data"])