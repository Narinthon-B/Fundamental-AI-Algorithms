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

### Depth-First Search (DFS)
# set used to store visited nodes.
visitedNodes = []
# function
def dfs(visitedNodes, graph, node):
  if node not in visitedNodes:
    print(node)
    visitedNodes.append(node)

    for neigbor in graph[node]:
      dfs(visitedNodes, graph, neigbor)

# Main Code
node  = input("Enter Starting Node(A, B, C, D or E) :").upper()
# calling dfs function
print("\nRESULT :")
dfs(visitedNodes, graph, node)