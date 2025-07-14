# graph wit Dijstrak algorithm 
from heapq import heapify, heappop, heappush
graph = {
    "A":{"B" : 3, "C": 3},
    "B": {"A": 3, "D": 3.5, "E": 2.8},
    "C": {"A": 3, "E":2.5, "F": 3.5},
    "D" : {"B": 3.5, "E": 3.1, "G" : 10},
    "E" : {"B" : 2.8, "C": 2.8, "D": 3.1, "G": 7},
    "F" : {"G" : 2.5, "C": 3.5},
    "G" : {"F": 2.5, "E": 7, "D" : 10},
}


class Graph:
    def __init__(self, graph: dict = {}):
        self.graph = graph  #A dictionary for the adjacency list

    def add_edge(self, node1, node2, weight):
        if node1 not in self.graph: # Check if node is already added 
            self.graph[node1] = {} # if not , create the node
        
        self.graph[node1][node2] = weight # Else , add a connection to its neighbor


G = Graph()

# add A and its neighbors
G.add_edge("A", "B", 3 )
G.add_edge("A", "C" , 3)


# Add B and its neighbors
G.add_edge("B", "A" , 3)
G.add_edge("B", "D", 3.5)
G.add_edge("B", "E" , 2.8)

# or USe the dictionary we defined earlier 

G = Graph(graph = graph)

G.graph 

{'A': {'B': 3, 'C': 3},
'B': {'A': 3, 'D': 3.5, 'E': 2.8},
'C': {'A': 3, 'E': 2.8, 'F': 3.5},
'D': {'B': 3.5, 'E': 3.1, 'G': 10},
'E': {'B': 2.8, 'C': 2.8, 'D': 3.1, 'G': 7},
'F': {'G': 2.5, 'C': 3.5},
'G': {'F': 2.5, 'E': 7, 'D': 10}}


class Graph:
   def __init__(self, graph: dict = {}):
       self.graph = graph

   def shortest_distances(self, source: str):
       # Initialize the values of all nodes with infinity
       distances = {node: float("inf") for node in self.graph}
       distances[source] = 0  # Set the source value to 0

       # Initialize a priority queue
       pq = [(0, source)]
       heapify(pq)

       # Create a set to hold visited nodes
       visited = set()

       while pq:  # While the priority queue isn't empty
           current_distance, current_node = heappop(
               pq
           )  # Get the node with the min distance

           if current_node in visited:
               continue  # Skip already visited nodes
           visited.add(current_node)  # Else, add the node to visited set
           for neighbor, weight in self.graph[current_node].items():
            # Calculate the distance from current_node to the neighbor
                tentative_distance = current_distance + weight
                if tentative_distance < distances[neighbor]:
                    distances[neighbor] = tentative_distance
                    heappush(pq, (tentative_distance, neighbor))

           return distances

G = Graph(graph)

distances = G.shortest_distances("B")
print(distances, "\n")

to_F = distances["F"]
print(f"The shortest distance from B to F is {to_F}")



