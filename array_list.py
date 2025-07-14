# crate an empty array list then add temperature 35

temperature = []
temperature.append(35)
print(temperature)

# linkedlist 
class Node:
    def __init__(self, value, next_node):
        self.value = value
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.first_node = None
        self.last_node = None

    def append(self, value):
        node = Node(value, None)
        if self.first_node is None:
            self.first_node = node
            self.last_node = node
        else:
            self.last_node.next_node = node
            self.last_node = node