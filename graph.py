import random

class Graph:
    def __init__(self):
        self.graph = {}

    # Adding a node to the graph
    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    # Adding an edge to the graph (undirected for now)
    def add_edge(self, node1, node2):
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    # Returning neighbors of a node
    def get_neighbors(self, node):
        return self.graph[node]

    # For debugging and seeing the graph structure
    def display(self):
        for node, neighbors in self.graph.items():
            print(f'{node}: {neighbors}')

def splatter_nodes(nodes):
    """Randomly assign positions to nodes across the screen."""
    positions = {}
    for node in nodes:
        x = random.randint(100, 700)  # Adjust the range to fit within screen width (e.g., between 100 and 700 pixels)
        y = random.randint(100, 500)  # Adjust the range to fit within screen height (e.g., between 100 and 500 pixels)
        positions[node] = (x, y)
    return positions