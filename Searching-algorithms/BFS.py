import networkx as nx
import matplotlib.pyplot as plt
# Input Graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D', 'X'],
    'C': ['A', 'B', 'E','O'],
    'D': ['B', 'E'],
    'E': ['C', 'D'],
    'X': ['B'],
    'O': ['C']
}
# Create Graph object
G = nx.Graph()
# Add edges from directionary
for node in graph:
  for neigbor in graph[node]:
    G.add_edge(node, neigbor)

# Define position of node
pos = nx.spring_layout(G)
# Draw the graph
plt.figure(figsize=(6,6))
nx.draw(
    G, pos,
    with_labels=True,
    node_size=2000,
    node_color='#8d1b23',
    font_color='white',
    font_size=14,
    edge_color="gray"
)
plt.title("Graph Representation Searching Algorithm", fontsize=14)
plt.show()

### Bresdth-First Search (BFS)
# To store visited nodes.
visitedNodes = []
# To store nodes in queue
queueNodes = []
# function
def bfs(visitedNodes, graph, snode):
  visitedNodes.append(snode)
  queueNodes.append(snode)

  while queueNodes:
    m = queueNodes.pop(0)
    print(m)
    for neigbor in graph[m]:
      if neigbor not in visitedNodes:
        visitedNodes.append(neigbor)
        queueNodes.append(neigbor)
# Main Code
snode = input("Enter Starting Node(A, B, C, D or E) :").upper()
# calling bfs function
print("\nRESULT :")
bfs(visitedNodes, graph, snode)